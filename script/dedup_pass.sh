#!/bin/sh
# One dedup pass over Nord calendar (calendar 1), Fall-2026 window, courses EK369E/EK342E/FIN5005.
# Policy: within a (course,start,end) slot keep the "Code: Forelesning" (colon) copy if present,
# else keep one plain copy. Deletes the rest.
S="$1"
osascript "$S/verify.applescript" > "$S/pass.txt" 2>&1 || { echo "scan failed"; exit 1; }
python3 - "$S/pass.txt" "$S" <<'PY'
import sys,re,collections
src,out=sys.argv[1],sys.argv[2]
rows=[]
for line in open(src):
    line=line.rstrip("\n")
    if not line.strip(): continue
    p=line.split(" ||| ")
    if len(p)<5: continue
    summ,start,end,uid=p[1],p[2],p[3],p[4]
    m=re.search(r'(EK369E|EK342E|FIN5005)',summ)
    if not m: continue
    course=m.group(1)
    rows.append(dict(summ=summ,start=start,end=end,uid=uid,course=course,
                     variant="B" if re.search(course+r':',summ) else "A"))
g=collections.defaultdict(list)
for r in rows: g[(r['course'],r['start'],r['end'])].append(r)
delete=[]
for k,v in sorted(g.items()):
    if len(v)==1: continue
    bs=[r for r in v if r['variant']=="B"]
    keeper=bs[0] if bs else v[0]
    delete+= [r for r in v if r['uid']!=keeper['uid']]
print(f"scanned={len(rows)} slots={len(g)} to_delete={len(delete)}")
for r in delete: print(f"  DEL {r['course']} {r['start']}  {r['summ']}")
open(f"{out}/pass_uids.txt","w").write("\n".join(r['uid'] for r in delete)+("\n" if delete else ""))
PY
n=$(grep -c . "$S/pass_uids.txt" 2>/dev/null); [ -n "$n" ] || n=0
if [ "$n" -gt 0 ]; then
  { printf 'set uidList to {'
    awk 'NF{printf "%s\"%s\"", (NR>1?", ":""), $0}' "$S/pass_uids.txt"
    printf '}\n'
    printf 'set okCount to 0\nset failList to ""\ntell application "Calendar"\n\ttell calendar 1\n\t\trepeat with u in uidList\n\t\t\ttry\n\t\t\t\tdelete (first event whose uid is (u as string))\n\t\t\t\tset okCount to okCount + 1\n\t\t\ton error errm\n\t\t\t\tset failList to failList & (u as string) & " -> " & errm & linefeed\n\t\t\tend try\n\t\tend repeat\n\tend tell\nend tell\nreturn "deleted=" & okCount & " failures:" & failList\n'
  } > "$S/pass_del.applescript"
  osascript "$S/pass_del.applescript" 2>&1
else
  echo "nothing to delete"
fi
