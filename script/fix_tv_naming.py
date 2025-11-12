#!/usr/bin/env python3
"""
Fix TV show file naming to conform to standard conventions.

Standard format: ShowName.Year.S01E01.ext
Common issues:
- S01EP1 should be S01E01
- Episode numbers should be zero-padded (E1 -> E01)
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path
from typing import List, Tuple


def fix_episode_format(filename: str) -> str:
    """
    Fix episode format in filename.
    S01EP1 -> S01E01
    S01E1 -> S01E01
    """
    # Pattern: S(\d+)EP(\d+) -> S(\d+)E(\d+)
    pattern1 = re.compile(r'(S\d+)EP(\d+)', re.IGNORECASE)
    match = pattern1.search(filename)
    if match:
        season = match.group(1).upper()
        episode = match.group(2).zfill(2)  # Zero-pad to 2 digits
        new_format = f"{season}E{episode}"
        return pattern1.sub(new_format, filename)
    
    # Pattern: S(\d+)E(\d) -> S(\d+)E(\d\d) (ensure zero-padding)
    pattern2 = re.compile(r'(S\d+)E(\d)(?!\d)', re.IGNORECASE)
    match = pattern2.search(filename)
    if match:
        season = match.group(1).upper()
        episode = match.group(2).zfill(2)
        new_format = f"{season}E{episode}"
        return pattern2.sub(new_format, filename)
    
    return filename


def plan_renames(directory: Path) -> List[Tuple[Path, Path]]:
    """Find files that need renaming."""
    renames: List[Tuple[Path, Path]] = []
    
    for file in directory.iterdir():
        if file.is_file() and not file.name.startswith('.'):
            new_name = fix_episode_format(file.name)
            if new_name != file.name:
                new_path = file.parent / new_name
                if not new_path.exists():
                    renames.append((file, new_path))
                else:
                    print(f"  Warning: Cannot rename {file.name} - destination exists")
    
    return renames


def main() -> int:
    parser = argparse.ArgumentParser(description='Fix TV show file naming conventions')
    parser.add_argument('--dir', required=True, help='Directory containing TV show files')
    parser.add_argument('--apply', action='store_true', help='Apply renames (default is dry-run)')
    args = parser.parse_args()
    
    directory = Path(args.dir).expanduser().resolve()
    
    if not directory.exists() or not directory.is_dir():
        print(f"ERROR: Directory not found: {directory}")
        return 2
    
    renames = plan_renames(directory)
    
    if not renames:
        print("No files need renaming. All files conform to naming conventions.")
        return 0
    
    print(f"Found {len(renames)} files to rename:\n")
    for old, new in renames:
        print(f"  {old.name}")
        print(f"    -> {new.name}")
        print()
    
    if not args.apply:
        print("Dry-run complete. Re-run with --apply to perform renames.")
        return 0
    
    # Apply renames
    print("Applying renames...")
    for old, new in renames:
        try:
            old.rename(new)
            print(f"  Renamed: {new.name}")
        except Exception as e:
            print(f"  Failed to rename {old.name}: {e}")
    
    print("\nRename complete.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
