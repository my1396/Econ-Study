---
layout: post
tag: python
title: Python Strings
date: 2026-03-17
---

<a class="top-link hide" href="#" id="js-top">↑</a>

## f-strings

`f"..."` Allows you to embed Python expressions inside strings using `{}`.

`f"..."` is equivalent to `str.format()`, but more concise and easier to read.

```python
name = "Alice"
age = 30

# f-string
message = f"My name is {name} and I'm {age} years old"
# Result: "My name is Alice and I'm 30 years old"

# Equivalent to str.format(), but more verbose
message = "My name is {} and I'm {} years old".format(name, age)

# Can include expressions
message = f"Next year I'll be {age + 1}"
# Result: "Next year I'll be 31"

# Can format strings
price = 19.9999999
message = f"Price: ${price:.2f}"
# Result: "Price: $20.00"
```

f-strings can be used together with `=` specifier to <span class="env-green">print both the expression and its value</span>, which is very useful for debugging.

```python
x = 10
print(f"{x=}")  # Output: x=10
print(f"{x*2=}")  # Output: x*2=20
```

To format numbers, use `:` followed by format specifiers. E.g., `:.2f` formats a float to 2 decimal places.



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
username = "Alice"
# rf or fr - raw f-string (both raw AND formatted)
path = rf"C:\Users\{username}\Desktop"
```


--------------------------------------------------------------------------------

## Triple-quoted strings

`"""..."""` or `'''...'''` allows you to create multi-line strings without needing `\n`.

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

Triple-quoted strings will preserve your newlines and indentation. You don't need to use escape characters, e.g., `\n`, to create newlines. 

```python
>>> triple_quoted = """This is a triple-quoted string.
... It can span multiple lines.
... You can include 'single' and "double" quotes without any issues."""

>>> print(triple_quoted)
This is a triple-quoted string.
It can span multiple lines.
You can include 'single' and "double" quotes without any issues.
```

--------------------------------------------------------------------------------

**ref:**

- [DataCamp: Python f-string: A Complete Guide](https://www.datacamp.com/tutorial/python-f-string?utm_cid=23340058065&utm_aid=192632748929&utm_campaign=230119_1-ps-dscia~dsa-tofu~python_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&utm_loc=1010988-&utm_mtd=-c&utm_kw=&utm_source=google&utm_medium=paid_search&utm_content=ps-dscia~emea-en~dsa~tofu~tutorial~python&gad_source=1&gad_campaignid=23340058065&gbraid=0AAAAADQ9WsHy7AU1kaq4NlSB8WfSuXt3Y&gclid=EAIaIQobChMIwd7ItbWrkwMVshqiAx3LQQp4EAAYASAAEgLDhPD_BwE)

