---
layout: post
tag: python
title: Python Jupyter Notebook
date: 2026-02-01
---

This post introduces how to run Python code in Jupyter Notebook in VS Code, and the difference between Jupyter Notebook and Python script (.py file).

For running Python scripts in VS Code, see <a href="{{site.baseurl}}/2026/03/18/Python-VSCode.html">Python in VS Code</a>.


**Useful resources:**

- [R Notes: Jupyter Notebook](https://my1396.github.io/R-Notes/2.10-vs-code.html#jupyter-notebooks) for more tips on using Jupyter Notebook in VS Code.

--------------------------------------------------------------------------------

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
    
    People don't need to run the code to see the results, which is good for sharing and presentation. 
    You can also add markdown cells to explain your code and results, making it more readable and easier to understand.
  - But difficult to debug and writing code
  - Useful when you share with others for <span class="env-green">presentation purpose</span>
  - <span class="env-green">GitHub supports rendering `.ipynb` files</span> as of 2026. Takes a bit time to load.
    
    The difference preview is ok, but not so straightforward.

- **Python script**:
  
  - Use Python script for early stage when you write a lot of code and need to debug
  - You can use "Rename symbol" and to find and replace variables easily; just easier to debug
  - Once code is stable, you can copy the code to Jupyter Notebook for better presentation
  - When you share with others for <span class="env-green">collaboration purpose</span>


|      | Jupyter Notebook (.ipynb) | Python Script (.py) |
| ---- | ------------------------- | ------------------- |
| Pros | - Good for presentation;<br> - Save result output together with code; <br> - Don't need to run the code to have a preview of the results; <br> - Magic commands support; | - Good for development and debugging; <br> - Easy for versional control; |
| Cons | - Difficult to debug and write code;<br> - Difficult to do version control | - Less visually appealing for sharing results |

**Suggested workflow:**

- Start with a Python script for development and debugging.
- Once the code is stable, convert it to a Jupyter Notebook for better presentation and sharing.
  
  Open Command Palette (⇧⌘P) → "Jupyter: Export Current Python File as Jupyter Notebook" to convert a Python script to a Jupyter Notebook.

--------------------------------------------------------------------------------

## Export to Python script

In Jupyter Notebook, click the "..." button and choose "Export". A dropdown menu shows up in the command palette, select "Python Script".

Alternatively, you can use the command palette (⇧⌘P) and type "Jupyter: Export to Python Script" to export the current notebook to a Python script. 

You need to manually deal with the magic commands as they are not supported in Python scripts. 





