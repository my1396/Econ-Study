---
layout: post
tag: python
title: Python Scripts in VS Code
date: 2026-02-01
---

<a class="top-link hide" href="#" id="js-top">↑</a>

This post introduces how to run Python Scripts (.py files) in VS Code.

When I use ⇧Enter to run python code in selection, it evokes the python version different than the one I specified in the terminal.

The reason is that VS Code configures independently from the terminal. You can check your VS Code Python interpreter by looking at the bottom-right corner of VS Code. You will see sth like `Python 3.14.2`. Click on it, and you can select the Python interpreter (e.g., anaconda python) you want to use for your VS Code environment. 


Run selected code in Python terminal: 

1. Select the code you want to run.
2. Press ⇧⌘P to open the command palette, type "Run Selection in Python Terminal", and hit Enter. Or use keyboard shortcut ⇧Enter.

If the code is sent directly to the terminal without using the Python interpreter, you need to change [`terminal.integrated.inheritEnv`](https://code.visualstudio.com/updates/v1_36#_launch-terminals-with-clean-environments) in your VS Code settings (settings.json):

```json
"terminal.integrated.inheritEnv": false,
```

This setting ensures that the terminal does not inherit the environment variables from VS Code, allowing it to use the correct Python interpreter specified in your terminal. After adding this setting, reload the window and try running your code again. It should now use the correct Python version as specified in your terminal. You must see `>>>` in the terminal before sending code.

--------------------------------------------------------------------------------

## Run Python in Interactive Window

You can use `# %%` to create code cells in your Python file. Note the space between `#` and `%%`. This is a nice way to group your code into sections and run them separately. It resembles Jupyter Notebook style, but you can still keep the .py file format. It has a nice balance btw the flexibility of `.py` files and the interactivity of notebooks.

- You can add comments after `# %%` to give a title to the cell, e.g. `# %% Data Loading`.
- You don't have to use cells in order to run code in the interactive window. You can select any code snippet and run it in the interactive window by using the command palette and type "Jupyter: Run Selection/Line in Interactive Window" or use the keyboard shortcut ⇧Enter.

I changed the keyboard shortcuts for run selection in interactive window. It essentially uses a Jupyter kernel.

```json
{
  // run selection or current line
  "key": "shift+enter",
  "command": "jupyter.execSelectionInteractive",
  "when": "editorTextFocus && editorLangId == 'python'"
},
{
  // run current cell
  "key": "shift+cmd+enter",
  "command": "jupyter.runcurrentcell",
  "when": "editorTextFocus && editorLangId == 'python'"
},
{
  "key": "shift+enter",
  "command": "-jupyter.runcurrentcell"
}
```

| Keyboard Shortcut     | Action                                     |
| --------------------- | ------------------------------------------ |
| ⇧Enter                | Run selection in interactive window        |
| ⇧⌘Enter               | Run current cell in interactive window     |
| ⌥Enter                | Run current cell and insert new cell below |

One benefit of using interactive window is that it allows you to inspect variables and outputs in a more organized way. You can open the variable explorer in the buttom terminal and the output will be displayed in the interactive window. 

Also you can type directly in the interactive window to inspect variables. Just type your code snippet in the interactive window cell and hit Enter to run it.

<img src="https://drive.google.com/thumbnail?id=1IyH46i-i8dxgSDLmbLkpK5mySjTovyLA&sz=w1000" alt="" style="display: block; margin-right: auto; margin-left: auto; zoom:100%;" />


`X Clear All` will clear only the output, will not clear the variables.

`Restart` will clear the variables and output.


In a code cell, if you don't explicitly print the output, it will only show the last line of the cell. If you want to see the output of multiple lines, you need to use `print()` function.

```python
# This will only show the output of the last line
a = 10
b = 20
a + b  # Only this output will be shown 

# This will show the output of all lines
a = 10
b = 20
print(a)  # Output: 10
print(b)  # Output: 20
print(a + b)  # Output: 30
```