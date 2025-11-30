#!/usr/bin/env python3
"""
Format markdown tables with custom column widths.
Usage: python format_table.py <file_path> <start_line> <end_line> [col1_width] [separator_col]

Default: col1_width=38, separator_col=40, total_row_width=80
"""

import re
import sys
import unicodedata


def display_width(text):
    """
    Calculate the display width of text, accounting for wide characters.
    East Asian characters count as 2, others as 1.
    """
    width = 0
    for char in text:
        if unicodedata.east_asian_width(char) in ('F', 'W'):
            width += 2
        else:
            width += 1
    return width


def pad_to_width(text, target_width):
    """
    Pad text with spaces to reach target display width.
    """
    current_width = display_width(text)
    if current_width >= target_width:
        return text
    return text + ' ' * (target_width - current_width)


def format_table_row(line, col1_width=38, separator_col=40):
    """
    Format a single table row with specified column widths.
    
    Args:
        line: The line to format
        col1_width: Width for first column (default 38)
        separator_col: Position where second separator should be (default 40)
    
    Returns:
        Formatted line string
    """
    # Skip empty lines
    if not line.strip():
        return line
    
    # Skip lines that don't start with |
    if not line.strip().startswith('|'):
        return line
    
    # Handle separator rows (lines with only |, -, :, and spaces)
    if re.match(r'^\s*\|[\s\-:]+\|[\s\-:]+\|', line):
        # Format separator to match column widths: col1_width + col2_width with total 80
        col2_width = 80 - col1_width - 8
        return f"| {'-' * col1_width} | {'-' * col2_width} |"
    
    # Parse the columns by splitting on |
    parts = line.split('|')
    if len(parts) < 3:
        return line
    
    # Extract column content (strip whitespace)
    col1 = parts[1].strip() if len(parts) > 1 else ''
    col2 = parts[2].strip() if len(parts) > 2 else ''
    
    # Calculate display width (accounting for wide characters)
    col1_display = display_width(col1)
    col2_display = display_width(col2)
    
    # Calculate total width with minimal spacing
    # Format: "| content | content |"
    # Width = 1 + 1 + display_width(col1) + 1 + 1 + 1 + display_width(col2) + 1 + 1
    min_width = col1_display + col2_display + 8
    
    # If the total would exceed 80 characters, use minimal spacing
    if min_width > 80:
        return f"| {col1} | {col2} |"
    
    # Otherwise, format with fixed column widths
    # col2_width is calculated to make the row end at column 80
    # Total: 1 + 1 + col1_width + 1 + 1 + 1 + col2_width + 1 + 1 = 80
    # So: col2_width = 80 - col1_width - 8
    col2_width = 80 - col1_width - 8
    
    # Pad columns to their target display widths
    col1_padded = pad_to_width(col1, col1_width)
    col2_padded = pad_to_width(col2, col2_width)
    
    return f"| {col1_padded} | {col2_padded} |"


def format_table(file_path, start_line, end_line, col1_width=38, separator_col=40):
    """
    Format a table in a markdown file.
    
    Args:
        file_path: Path to the markdown file
        start_line: Starting line number (1-indexed)
        end_line: Ending line number (1-indexed, inclusive)
        col1_width: Width for first column (default 38)
        separator_col: Position where second separator should be (default 40)
    """
    # Read the entire file
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Format the specified range
    for i in range(start_line - 1, end_line):
        if i < len(lines):
            lines[i] = format_table_row(lines[i], col1_width, separator_col) + '\n'
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(lines)
    
    print(f"Completed: Aligned table rows {start_line}-{end_line} with separator at column {separator_col}")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python format_table.py <file_path> <start_line> <end_line> [col1_width] [separator_col]")
        print("Example: python format_table.py file.md 100 150 38 40")
        sys.exit(1)
    
    file_path = sys.argv[1]
    start_line = int(sys.argv[2])
    end_line = int(sys.argv[3])
    col1_width = int(sys.argv[4]) if len(sys.argv) > 4 else 38
    separator_col = int(sys.argv[5]) if len(sys.argv) > 5 else 40
    
    format_table(file_path, start_line, end_line, col1_width, separator_col)
