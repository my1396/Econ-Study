---
layout: post
tag: python
title: Python Strings
date: 2026-03-17
---

<a class="top-link hide" href="#" id="js-top">↑</a>

## f-strings

`f"..."` Allows you to embed Python expressions inside strings using `{}`.

```python
name = "Alice"
age = 30

# f-string
message = f"My name is {name} and I'm {age} years old"
# Result: "My name is Alice and I'm 30 years old"

# Can include expressions
message = f"Next year I'll be {age + 1}"
# Result: "Next year I'll be 31"

# Can call functions
price = 19.99
message = f"Price: ${price:.2f}"
# Result: "Price: $19.99"
```

--------------------------------------------------------------------------------

## r-strings

`r"..."` Does NOT interpret escape sequences. E.g., treats backslashes `\` as literal characters.

Raw strings are useful for file paths. This is especially helpful on Windows where backslashes are common in paths, though less critical on Unix/Mac since forward slashes don't need escaping.

```python
# Normal string - \n is interpreted as newline
path1 = "C:\new\test"  # Problem! \n becomes newline, \t becomes tab

# Raw string - \n stays as \n
path2 = r"C:\new\test"  # Correct! Keeps backslashes
# Result: "C:\new\test"

# Windows file paths
file_path = r"C:\Users\menghan\Desktop\file.csv"

# Regex patterns
pattern = r"\d{3}-\d{4}"  # Matches phone numbers like 123-4567
```

`rf"..."` Combines raw and f-string features. You can include expressions and also treat backslashes as literal characters.

```python
username = "menghan"
# rf or fr - raw f-string (both raw AND formatted)
path = rf"C:\Users\{username}\Desktop"
```


--------------------------------------------------------------------------------

## Triple-quoted strings

`"""..."""` or `'''...'''` Allows you to create multi-line strings without needing `\n`.

This is useful for SQL queries which often span multiple lines for readability.

```python
# SQL query with f-string and triple quotes
query = f"""
SELECT *
FROM table
WHERE date = '{my_date}'
"""

# Return results as a DataFrame
res = conn.execute(query).df()
```