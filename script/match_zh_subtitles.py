#!/usr/bin/env python3
"""
Match Chinese subtitle files to video files and rename/relocate them.

Requirements:
- Match .ass subtitle files to .mp4 video files by episode number
- Rename to match video filename pattern
- Add language code before extension: video.zh.ass
- Copy to video directory

Usage:
  python3 script/match_zh_subtitles.py \
    --video-dir "/path/to/videos" \
    --subs-dir "/path/to/zh/subtitles" \
    --lang zh \
    --dry-run

  python3 script/match_zh_subtitles.py \
    --video-dir "/path/to/videos" \
    --subs-dir "/path/to/zh/subtitles" \
    --lang zh \
    --apply
"""
from __future__ import annotations
import argparse
import re
import shutil
from pathlib import Path
from typing import List, Tuple, Optional


def extract_episode_number(filename: str) -> Optional[str]:
    """
    Extract episode number pattern like S01E01.
    """
    m = re.search(r'(S\d+E\d+)', filename, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    return None


def find_videos(video_dir: Path) -> dict[str, Path]:
    """
    Find all video files and map by episode number.
    Returns: {episode_number: video_path}
    """
    videos = {}
    for item in video_dir.iterdir():
        if item.is_file() and item.suffix.lower() in {'.mp4', '.mkv', '.avi'}:
            ep_num = extract_episode_number(item.name)
            if ep_num:
                videos[ep_num] = item
    return videos


def find_subtitles(subs_dir: Path, subtitle_ext: str = '.ass') -> dict[str, Path]:
    """
    Find all subtitle files and map by episode number.
    Returns: {episode_number: subtitle_path}
    """
    subtitles = {}
    for item in subs_dir.iterdir():
        if item.is_file() and item.suffix.lower() == subtitle_ext.lower():
            ep_num = extract_episode_number(item.name)
            if ep_num:
                subtitles[ep_num] = item
    return subtitles


def plan_subtitle_copies(video_dir: Path, subs_dir: Path, lang_code: str, subtitle_ext: str = '.ass') -> Tuple[List[Tuple[Path, Path]], List[str]]:
    """
    Plan subtitle file copies with proper naming.
    Returns: (list of (src, dest) tuples, list of unmatched episode numbers)
    """
    videos = find_videos(video_dir)
    subtitles = find_subtitles(subs_dir, subtitle_ext)
    
    copies: List[Tuple[Path, Path]] = []
    unmatched: List[str] = []
    
    for ep_num in sorted(videos.keys()):
        video = videos[ep_num]
        if ep_num in subtitles:
            subtitle = subtitles[ep_num]
            # Create destination: video_name.lang.ext
            # e.g., Prison.Break.S01E01.1080p.BluRay.x265-RARBG.zh.ass
            dest = video.with_suffix(f'.{lang_code}{subtitle_ext}')
            copies.append((subtitle, dest))
        else:
            unmatched.append(ep_num)
    
    return copies, unmatched


def main() -> int:
    parser = argparse.ArgumentParser(description='Match and rename Chinese subtitle files for videos')
    parser.add_argument('--video-dir', required=True, help='Directory containing video files')
    parser.add_argument('--subs-dir', required=True, help='Directory containing subtitle files')
    parser.add_argument('--lang', default='zh', help='Language code (default: zh)')
    parser.add_argument('--sub-ext', default='.ass', help='Subtitle file extension (default: .ass)')
    parser.add_argument('--apply', action='store_true', help='Apply changes (default is dry-run)')
    args = parser.parse_args()
    
    video_dir = Path(args.video_dir).expanduser().resolve()
    subs_dir = Path(args.subs_dir).expanduser().resolve()
    
    if not video_dir.exists():
        print(f"ERROR: Video directory not found: {video_dir}")
        return 2
    
    if not subs_dir.exists():
        print(f"ERROR: Subtitles directory not found: {subs_dir}")
        return 2
    
    copies, unmatched = plan_subtitle_copies(video_dir, subs_dir, args.lang, args.sub_ext)
    
    print(f"Found {len(copies)} subtitle matches")
    if unmatched:
        print(f"Unmatched episodes: {len(unmatched)}")
    print()
    
    if copies:
        print("Planned operations:")
        for src, dest in copies:
            print(f"  {src.name}")
            print(f"    -> {dest.name}")
            print()
    
    if unmatched:
        print("Unmatched episodes:")
        for ep in unmatched:
            print(f"  {ep}")
        print()
    
    if not args.apply:
        print("Dry-run complete. Re-run with --apply to copy and rename files.")
        return 0
    
    # Apply copies
    print("Applying operations...")
    for src, dest in copies:
        try:
            if dest.exists():
                print(f"  Skipping (destination exists): {dest.name}")
                continue
            shutil.copy2(src, dest)
            print(f"  Copied: {dest.name}")
        except Exception as e:
            print(f"  Failed to copy {src} -> {dest}: {e}")
    
    print("\nOperation complete.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
