---
layout: post
tag: python
title: Python Pandas
date: 2026-03-18
---

## Pandas

[Documentation](https://pandas.pydata.org/docs/reference/frame.html)

Subset columns

`df[[col1, col2]]` returns a DataFrame with only the specified columns.

Select one column

`df[col]` returns a 1D <span class="env-green">Series</span> representing the specified column. 

`df[[col]]` returns a 2D <span class="env-green">DataFrame</span> with one column. 

To filter rows based on column values, use boolean indexing:

```python
# Filter rows where 'age' > 30
filtered_df = df[df['age'] > 30]
```

Note you have to use `df['age']` the single bracket notation to access the column for boolean indexing. 

If you want selected columns and filter rows at the same time, you can combine them:

```python
# Select 'name' and 'age' columns, and filter rows where 'age' > 30
result = df.loc[df['age'] > 30, ['name', 'age']]
```

Note that `df.loc[rows, columns]` allows you to use bollean indexing for rows and specify columns at the same time. The first argument is for row selection, and the second argument is for column selection.


`df.iloc[row_index, column_index]` is used for integer-based indexing, where you specify the row and column positions. For example, `df.iloc[0, 1]` will return the value in the first row and second column of the DataFrame.