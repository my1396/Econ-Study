---
layout: post
tag: programming
title: Python Jupyter Notebook
date: 2026-02-01
---


Q: Difference between `!pip install package` and `%pip install package` in Jupyter Notebook?  
A: The `%` magic commands ensure the package is installed in the correct **environment** that's running your notebook kernel, while `!` commands run in a **shell** that might use a different environment.


Q: Should I use `%conda install package` or `%pip install package` in Jupyter Notebook?  
A: If your Jupyter kernel is using a Conda environment, it's generally better to use `%conda install package` to ensure compatibility with other packages in that environment. However, if the package is not available via Conda, you can use `%pip install package` as a fallback.


`%conda` Run the conda package manager within the current kernel.

`%conda install [pkgs]` Install packages into the current conda environment.




[Built-in magic commands in Jupyter](https://ipython.readthedocs.io/en/stable/interactive/magics.html)

--------------------------------------------------------------------------------

When to use Jupyter Notebook vs. Python script (`.py` file):

- **Jupyter Notebook**:
  - Good to put results and code together
  - But difficult to debug and writing code
  - When you share with others for <span class="env-green">presentation purpose</span>
- **Python script**:
  - Use Python script for early stage when you write a lot of code and need to debug
  - You can use "Rename symbol" and to find and replace variables easily; just easier to debug
  - Once code is stable, you can copy the code to Jupyter Notebook for better presentation
  - When you share with others for <span class="env-green">collaboration purpose</span>

--------------------------------------------------------------------------------

## Pandas

[Documentation](https://pandas.pydata.org/docs/reference/frame.html)