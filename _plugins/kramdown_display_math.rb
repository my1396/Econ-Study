# frozen_string_literal: true

# Render `$$ ... $$` as display math whenever the delimiters sit on their own
# lines, even when the block is not surrounded by blank lines.
#
# Stock kramdown only treats `$$ ... $$` as a math *block* when it is separated
# from the surrounding text by blank lines. Otherwise the `$$` lines are
# absorbed into the neighbouring paragraph and parsed as *span* math, which the
# MathJax engine emits as `\( ... \)`, so MathJax renders it inline.
#
# This patch makes the GFM parser (`kramdown: input: GFM` in _config.yml)
#   1. end a paragraph before a line that starts with `$$` whose closing `$$`
#      is the last thing on its line, and
#   2. accept such a `$$ ... $$` as block math whatever precedes or follows it.
# `$$ ... $$` used within a sentence is unaffected and stays inline.

require "kramdown/parser/gfm"

module DisplayMathOnOwnLines
  # `$$` at line start, no `$$` inside, closing `$$` at line end
  DISPLAY_MATH_START = /^[ ]{0,3}\$\$(?:(?!\$\$).)*\$\$[ \t]*\n/m

  def paragraph_end
    @display_math_paragraph_end ||= Regexp.union(super, DISPLAY_MATH_START)
  end

  def parse_block_math
    # @src holds the BLOCK_MATH_START match: [1] escape, [2] body, [3] line end
    return super if @src[1] || !@src[3]

    start_line_number = @src.current_line_number
    data = @src[2].strip
    @src.pos += @src.matched_size
    @tree.children << new_block_el(:math, data, nil, category: :block, location: start_line_number)
    true
  end
end

Kramdown::Parser::GFM.prepend(DisplayMathOnOwnLines)
