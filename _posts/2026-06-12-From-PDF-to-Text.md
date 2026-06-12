---
layout: post
title: Extract text from PDF
tag: python
date: 2026-06-12
---

Based on two Python libraries, `pymupdf` and `camelot`.

- [`pymupdf`](https://github.com/pymupdf/pymupdf) can extract text and create a screenshot of defined area of a PDF page. It can also extract images.
- [`camelot`](https://github.com/camelot-dev/camelot) is good at identifying tables without visible borders. `camelot` identifies the coordinates of the table and then uses `pymupdf` to create a screenshot of the table area. 

For converting pdf to text, I first create a visual environment

```bash
conda create -name pdf2text python=3.11 -y
```

Then I install the two libraries in the environment:

```bash
conda activate pdf2text
pip install pymupdf camelot-py
```