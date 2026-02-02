#!/bin/bash
# Script to export HTML to PDF with math rendering via Prince XML

# If no arguments provided, show help message below.
# It provides usage instructions and an example command.
if [ $# -eq 0 ]; then
    echo "Usage: $0 <html-file>"
    echo "Example: $0 mypost.html"
    echo ""
    echo "Equivalent Prince command:"
    echo "  prince input.html -o output.pdf \\"
    echo "    --style https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css \\"
    echo "    --style ./assets/css/prince.css"
    echo ""
    echo "Note: You must first export your markdown to HTML using MPE"
    echo "      (Right-click in preview → Export → HTML)"
    exit 1
fi

HTML_FILE="$1"

# Check if input is .md file and warn user
if [[ "$HTML_FILE" == *.md ]]; then
    echo "Error: Please provide an HTML file, not a markdown file."
    echo ""
    echo "Steps:"
    echo "1. Open the markdown file in VS Code"
    echo "2. Right-click in the preview pane"
    echo "3. Select 'HTML' → 'HTML (offline)' to export"
    echo "4. Then run: $0 <exported-html-file>"
    exit 1
fi

PDF_FILE="${HTML_FILE%.html}.pdf"

# Check if HTML file exists
if [ ! -f "$HTML_FILE" ]; then
    echo "Error: File '$HTML_FILE' not found"
    exit 1
fi

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run Prince with KaTeX CSS and custom styles
prince "$HTML_FILE" -o "$PDF_FILE" \
    --style https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css \
    --style "$SCRIPT_DIR/assets/css/prince.css"

echo "PDF created: $PDF_FILE"
