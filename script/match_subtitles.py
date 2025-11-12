#!/usr/bin/env python3
"""
Match subtitle files with video files and rename/relocate them.

Requirements:
- Find .mp4 files in video directory
- Find matching .srt files in Subs/episode_name/ subdirectories
- Rename subtitle to video.en.srt format
- Move subtitle to same directory as video

Usage:
  python3 script/match_subtitles.py \
    --video-dir "/path/to/videos" \
    --subs-dir "/path/to/videosSubs" \
    --dry-run

  python3 script/match_subtitles.py \
    --video-dir "/path/to/videos" \
    --subs-dir "/path/to/videosSubs" \
    --apply
"""
from __future__ import annotations
import argparse
import os
import re
import shutil
from pathlib import Path
from typing import List, Tuple, Optional


def normalize_episode_name(s: str) -> str:
    """
    Normalize episode name for fuzzy matching.
    Remove common separators, lowercase, keep only alphanumeric.
    """
    # Replace common separators with space
    s = re.sub(r'[._\-\s]+', ' ', s.lower())
    # Remove everything that's not alphanumeric or space
    s = re.sub(r'[^a-z0-9\s]', '', s)
    # Collapse multiple spaces
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def extract_episode_number(filename: str) -> Optional[str]:
    """
    Extract episode number pattern like S01E01, 1x01, etc.
    """
    # Pattern for S01E01, s01e01
    m = re.search(r's(\d+)e(\d+)', filename.lower())
    if m:
        return f"s{m.group(1)}e{m.group(2)}"
    
    # Pattern for 1x01
    m = re.search(r'(\d+)x(\d+)', filename.lower())
    if m:
        season = m.group(1).zfill(2)
        episode = m.group(2).zfill(2)
        return f"s{season}e{episode}"
    
    return None


def find_videos(video_dir: Path) -> List[Path]:
    """Find all .mp4 files in video directory."""
    videos = []
    for item in video_dir.iterdir():
        if item.is_file() and item.suffix.lower() == '.mp4':
            videos.append(item)
    return sorted(videos)


def find_subtitle_folders(subs_dir: Path) -> List[Path]:
    """Find all episode folders in Subs directory."""
    folders = []
    if not subs_dir.exists():
        return folders
    for item in subs_dir.iterdir():
        if item.is_dir():
            folders.append(item)
    return sorted(folders)


def find_first_srt(folder: Path) -> Optional[Path]:
    """Find the first .srt file in a folder."""
    srt_files = sorted([f for f in folder.iterdir() if f.is_file() and f.suffix.lower() == '.srt'])
    return srt_files[0] if srt_files else None


def match_subtitle_to_video(video: Path, sub_folders: List[Path]) -> Optional[Path]:
    """
    Match a video file to a subtitle folder.
    Strategy:
    1. Try exact episode number match (S01E01)
    2. Try normalized name match
    """
    video_stem = video.stem
    video_norm = normalize_episode_name(video_stem)
    video_ep = extract_episode_number(video_stem)
    
    # Try episode number match first
    if video_ep:
        for folder in sub_folders:
            folder_ep = extract_episode_number(folder.name)
            if folder_ep and folder_ep == video_ep:
                return find_first_srt(folder)
    
    # Try normalized name match
    best_match = None
    best_score = 0
    
    for folder in sub_folders:
        folder_norm = normalize_episode_name(folder.name)
        # Simple scoring: count matching words
        video_words = set(video_norm.split())
        folder_words = set(folder_norm.split())
        if not video_words or not folder_words:
            continue
        common = video_words & folder_words
        score = len(common) / max(len(video_words), len(folder_words))
        
        if score > best_score and score > 0.3:  # At least 30% match
            srt = find_first_srt(folder)
            if srt:
                best_match = srt
                best_score = score
    
    return best_match


def plan_moves(video_dir: Path, subs_dir: Path) -> Tuple[List[Tuple[Path, Path]], List[Path]]:
    """
    Plan subtitle file moves.
    Returns: (list of (src, dest) tuples, list of unmatched videos)
    """
    videos = find_videos(video_dir)
    sub_folders = find_subtitle_folders(subs_dir)
    
    moves: List[Tuple[Path, Path]] = []
    unmatched: List[Path] = []
    
    for video in videos:
        subtitle = match_subtitle_to_video(video, sub_folders)
        if subtitle:
            # Create destination path: video.en.srt
            dest = video.with_suffix('.en.srt')
            moves.append((subtitle, dest))
        else:
            unmatched.append(video)
    
    return moves, unmatched


def main() -> int:
    parser = argparse.ArgumentParser(description='Match and relocate subtitle files for video files')
    parser.add_argument('--video-dir', required=True, help='Directory containing .mp4 files')
    parser.add_argument('--subs-dir', required=True, help='Directory containing Subs/episode_name/ folders')
    parser.add_argument('--apply', action='store_true', help='Apply changes (default is dry-run)')
    args = parser.parse_args()
    
    video_dir = Path(args.video_dir).expanduser().resolve()
    subs_dir = Path(args.subs_dir).expanduser().resolve()
    
    if not video_dir.exists():
        print(f"ERROR: Video directory not found: {video_dir}")
        return 2
    
    if not subs_dir.exists():
        print(f"ERROR: Subs directory not found: {subs_dir}")
        return 2
    
    moves, unmatched = plan_moves(video_dir, subs_dir)
    
    print(f"Found {len(moves)} subtitle matches")
    print(f"Unmatched videos: {len(unmatched)}")
    print()
    
    if moves:
        print("Planned moves:")
        for src, dest in moves:
            print(f"  {src.parent.name}/{src.name}")
            print(f"    -> {dest.name}")
            print()
    
    if unmatched:
        print("Unmatched videos:")
        for video in unmatched:
            print(f"  {video.name}")
    
    if not args.apply:
        print("\nDry-run complete. Re-run with --apply to perform moves.")
        return 0
    
    # Apply moves
    print("\nApplying moves...")
    for src, dest in moves:
        try:
            if dest.exists():
                print(f"  Skipping (destination exists): {dest.name}")
                continue
            shutil.copy2(src, dest)
            print(f"  Copied: {dest.name}")
        except Exception as e:
            print(f"  Failed to copy {src} -> {dest}: {e}")
    
    print("\nApply complete.")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
