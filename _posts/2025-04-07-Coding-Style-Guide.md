---
layout: post
title: Good Coding Practices
tag: programming
update: 2025-04-07
---

<a class="top-link hide" href="#" id="js-top">↑</a>

**Tips**:

- `.Rproj` 可以用起来
- 需要经常重启。\
    重启会删除一些中间存储变量，再次运行，确保代码正确，以及借此机会重新整理代码。

___

## Project Structure

**项目整体结构 project file structure**

- Avoid writing excessively long scripts; do one thing in one script; 一个文档做一件事  
  If it is difficult to understand your code without comments, this can indicate that your code is too complex and might benefit from being broken down, or ‘refactored’, into smaller units. 
  
    - Start with file description about what this file does, what output it generates; preferably add edit time;
        - Last edit: `yy-mm-dd` (ISO8601); to show when you change the script last time;
    - Date naming convention: `yy-mm-dd`; add date to output files to indicate historical versions;
- Script naming conventions: `1-1-1_function-of-script`; 
    - the first digit denote main procedures; the second denotes sub-procedures, the third denotes various versions;
    - `function-of-script` describes what the script does;  
    Should follow "Context + verb + noun". Scripts that belong to the same context should start with the same prefix, i.e., context.
    - 画图文件不要用图1，2，3来命名，因为后期可能调换位置。用图的内容命名。
    - If your file names include numbers, make sure to pad them with the appropriate number of zeros.

    ```
    # good file names
    01-load-data.R
    02-exploratory-analysis.R
    03-model-approach-1.R
    04-model-approach-2.R
    2025-01-01-report.Rmd
    2025-02-01.report.Rmd
    ```
    Don’t use “final” or similar words in file names. Put the date in the file name to indicate historical versions.
    ```
    # good
    report-2022-03-20.qmd
    report-2022-04-02.qmd
    
    # bad
    finalreport.qmd
    FinalReport-2.qmd
    ```

- Write project file structure guide; ReadMe file;
- When writing big projects, worth writing a notes of <span style='color:#00CC66'>important variables</span> to help keep track of things;
- Avoid repetition; organize codes frequently;  
- If something is not used but you want to keep it as a backup, label it as deprecated.


___

## Internal Structure

**具体每个 script**

- Name variables meaningfully; consistently (variables that hold the same type of things should have consistent naming with <span style='color:#00CC66'>suffix</span> to denote variations); 
- File path \
    Avoid using absolute path. Store file names in variables so you can change easily.
- If your script uses add-on packages, load them all at once at the very beginning of the file.   
    Do NOT use `library()` calls throughout your code or having hidden dependencies that are loaded in a startup file, such as `.Rprofile`. ❌
- Prefer `TRUE` and `FALSE` over `T` and `F`.

___

**Spacing**

- Place spaces around all infix operators (`=`, `+`, `-`, `<-`, etc. 中缀运算符). 
- The same rule applies when using `=` in function calls. 
- Always put a space after a comma, and never before.

    ```r
    # Good
    average <- mean(feet / 12 + inches, na.rm = TRUE)
    
    # Bad
    average<-mean(feet/12+inches,na.rm=TRUE)
    ```

There are **a few exceptions**, where infix operators should NEVER be surrounded by spaces:

- The operators with [high precedence](https://rdrr.io/r/base/Syntax.html) `:`, `::`, `:::`, `$`, `@`, `[`, `[[`, `^`, unary `-`, unary `+`, and `:`.

    ```r
    # Good
    sqrt(x^2 + y^2)
    df$z
    x <- 1:10

    # Bad
    sqrt(x ^ 2 + y ^ 2)
    df $ z
    x <- 1 : 10
    ```

- Single-sided formulas when the right-hand side is a single identifier.

    ```r
    # Good
    ~foo
    tribble(
    ~col1, ~col2,
    "a",   "b"
    )

    # Bad
    ~ foo
    tribble(
    ~ col1, ~ col2,
    "a", "b"
    )
    ```

- Note that single-sided formulas with a complex right-hand side do need a space.

    ```r
    # Good
    ~ .x + .y

    # Bad
    ~.x + .y
    ```

- When used in tidy evaluation `!!` (bang-bang) and `!!!` (bang-bang-bang) (because they have precedence equivalent to unary `-`/`+`).

    ```r
    # Good
    call(!!xyz)
    
    # Bad
    call(!! xyz)
    call( !! xyz)
    call(! !xyz)
    ```



___

**Code Sessions**

Another important use of comments is to break up your file into easily readable chunks. Use long lines of `-` and `=` to make it easy to spot the breaks.

```r
# Load data --------------------------------------

# Plot data ======================================
```

___

**Pipes**

- Migrate from `magrittr`’s `%>%` to the native pipe `|>`.
- Same keyboard shortcut: ⇧⌘M



___

**Parentheses**

Do not put spaces inside or outside parentheses for regular function calls.

```r
# Good
mean(x, na.rm = TRUE)

# Bad
mean␣(x, na.rm = TRUE)
mean(␣x, na.rm = TRUE␣)
```

Place a space before and after `()` when used with `if`, `for`, or `while`.

```r
# Good
if␣(debug)␣{
  show(x)
}

# Bad
if(debug){
  show(x)
}
```

Place a space after `()` used for function arguments:

```r
# Good
function(x)␣{}

# Bad
function (x) {}
function(x){}
```



___

The [embracing operator][embrace-operator], "\{\{" (curly-curly operator), should always have inner spaces to help emphasis its special behavior:

```r
# Good
max_by <- function(data, var, by) {
  data |>
    group_by({{␣by␣}}) |>
    summarise(maximum = max({{ var }}, na.rm = TRUE))
}

# Bad
max_by <- function(data, var, by) {
  data |>
    group_by({{by}}) |>
    summarise(maximum = max({{var}}, na.rm = TRUE))
}
```



___

Distinguish from **braced expressions**, `{}`

It allows you to group multiple R expressions together into a single expression. The most common places to use braced expressions are in function definitions, control flow, and in certain function calls (e.g. `tryCatch()` and `test_that()`).

To make this hierarchy easy to see:

- `{` should be the last character on the line.  
    Related code (e.g., an `if` clause, a function declaration, a trailing comma, …) must be on the same line as the opening brace.

- `}` should be the first character on the line.

```r
# Good
if (y < 0 && debug) {
  message("y is negative")
}

if (y == 0) {
  if (x > 0) {
    log(x)
  } else {
    message("x is negative or zero")
  }
} else {
  y^x
}

test_that("call1 returns an ordered factor", {
  expect_s3_class(call1(x, y), c("factor", "ordered"))
})

```






___

## Functions

- Function names should tell what the function does. It should be short, but it’s better to be clear than short, as coding editors’ autocomplete makes it easy to type long names.
- Function names should be verbs, and arguments should be nouns. 
- nouns are ok if the function computes a very well known noun. 
    - `mean()` is better than `compute_mean()` and  `coef()` is better than `get_coefficients()`
    - A good sign that a noun might be a better choice is if you’re using a very broad verb like “get”, “compute”, “calculate”, or “determine”. ❌

    ```r
    # Too short
    f()
    
    # Not a verb, or descriptive
    my_awesome_function()
    
    # Long, but clear
    impute_missing()
    collapse_years()
    ```

- “snake_case”, where each lowercase word is separated by an underscore.
    - "camelCase" is a popular alternative. 
    - It doesn’t really matter which one you pick, the important thing is to be consistent: pick one or the other and stick with it.

    ```r
    # Never do this!
    col_mins <- function(x, y) {}
    rowMaxes <- function(y, x) {}
    ```

    - If you have a family of functions that do similar things, make sure they have consistent names and arguments. \
        <span style='color:#00CC66'>Use a common prefix</span> to indicate that they are connected. That’s better than a common suffix because autocomplete allows you to type the prefix and see all the members of the family.
    
    ```r
    # Good
    input_select()
    input_checkbox()
    input_text()
    
    # Not so good
    select_input()
    checkbox_input()
    text_input()
    ```


- The arguments to a function typically fall into two broad sets: 
    - *Data arguments* supply the data to compute on, and 
    - *Detail arguments* supply arguments that control the details of the computation. 
    - Generally, data arguments should come first. Detail arguments should go on the end, and usually should have default values. 
    - *Arbitrary number of inputs*. When you see `…` (dot-dot-dot), it captures any number of arguments that aren’t otherwise matched.

In `mean(x, trim = 0, na.rm = FALSE)`, the data is `x`, and the details are how much data to trim from the ends (`trim`) and how to handle missing values (`na.rm`).

- The **default value** of detailed argument should almost always be the most common value. The few exceptions to this rule are to do with *safety*. For example, it makes sense for `na.rm` to default to `FALSE` because missing values are important. Even though `na.rm = TRUE` is what you usually put in your code, it’s a bad idea to silently ignore missing values by default.
- When you call a function, you typically 
    - omit the names of the data arguments, because they are used so commonly. 
    - If you override the default value of a detail argument, you should use the full name.

    ```r
    # Good
    mean(1:10, na.rm = TRUE)
    
    # Bad
    mean(x = 1:10, , FALSE)
    mean(, TRUE, x = c(1:10, NA))
    ```

- You can refer to an argument by its unique prefix (e.g. `mean(x, n = TRUE)`), but this is generally best avoided given the possibilities for confusion.


___

## Documenting Functions

**Comments**

- Capitalize first letter
- If 1 sentence, don’t add period; if >1 sentence, add period.
- Add a single space after `#`

Insert *Roxygen Comments*: ⇧⌥⌘R 

- Useful for R package documentation
- Similar to Python’s docstring
- Q: Can regular functions (not in a package) be documented using the same syntax?

The inserted code looks like this:

```r
#' @title Make shades (Title of the function)
#'
#' @description 
#' Given a colour make n lighter or darker shades (Detailed description of the function)
#'
#' @param colour The colour to make shades of
#' @param n The number of shades to make
#' @param lighter Whether to make lighter (TRUE) or darker (FALSE) shades
#'
#' @return A vector of n colour hex codes
#' @export
#'
#' @examples Provide some examples of how to use your function
#' # Five lighter shades
#' make_shades("goldenrod", 5)
#' # Five darker shades
#' make_shades("goldenrod", 5, lighter = FALSE)
make_shades <- function(colour, n, lighter = TRUE) {
    [your function code here ...]
}
```

Roxygen comments all start with `#'`. 

- Put at the top of your function.
- `@title`: The first line is the title of the function then there is a blank line. 
- `@description`: Following that there can be a paragraph giving a more detailed description of the function. 
- The keywords `@title` and `@description` can be left off (not the text, just the `@…` part), but title text should be in line 1, then a blank line (`#’` only), and then the description text.
- The next section describes the parameters (or arguments) for the function marked by the `@param` field.  
    Provide the type and a short description of function inputs.
- The next field is `@return`. This is where we describe what the function returns.  
    Provide the type and a short description of function outputs.
- `@export` adds your function to your NAMESPACE.  Adding `@export` tells Roxygen that this is a function that we want to be available to the user.
- `@examples` is where we put some short examples showing how the function can be used.  
    Which custom functions are called from this function (or from where was this function called - imagine a directed graph).

Another example of a function documented with Roxygen

```r
#' Plot colours
#'
#' Plot a vector of colours to see what they look like
#' 
#' @param colours Vector of colour to plot
#'
#' @return A ggplot2 object
#' @export
#'
#' @importFrom rlang .data
#' 
#' @examples
#' shades <- make_shades("goldenrod", 5)
#' plot_colours(shades)
plot_colours <- function(colours) {
    plot_data <- data.frame(Colour = colours)
    
    ggplot2::ggplot(plot_data,
                    ggplot2::aes(x = .data$Colour, y = 1, fill = .data$Colour,
                                 label = .data$Colour)) +
        ggplot2::geom_tile() +
        ggplot2::geom_text(angle = "90") +
        ggplot2::scale_fill_identity() +
        ggplot2::theme_void()
}
```


___

<p style="font-weight:600; font-size:21px">References:</p>

R for Data Scince, <https://r4ds.had.co.nz/functions.html>  
R package development workshop, <https://combine-australia.github.io/r-pkg-dev/other-documentation.html>  
Tidyverse Style Guide, <https://style.tidyverse.org>  
Python Style Guide, <https://peps.python.org/pep-0008/>  





[embrace-operator]: <https://rlang.r-lib.org/reference/embrace-operator.html>