---
layout: post
tag: python
title: Python Virtual Environment
date: 2026-03-17
---

## Virtural Environment

Python is shipped with the OS out of box for UNIX-based systems. If you run `which python`, you will see sth like `usr/bin/python3`, this is the system Python. It is NOT recommended to install packages in the system Python as it may cause <span class="env-green">conflicts with the OS and other applications that rely on it</span>. 
You might end up with some complicated fixes or fresh OS installation if you mess with the system Python.
Therefore, <span class="env-green">you should use a virtual environment to manage your project-specific dependencies</span>.


> Rule of thumb: Don't mess with the base environment of Conda or the system Python. 
> Always create a new virtual environment for each project to keep things clean and organized.

A virtual environment in Python is <span class="env-green">an isolated environment</span> on your computer. It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.


**Each virtual environment:**

- Has its own Python interpreter
- Has its own set of installed packages
- Is isolated from other virtual environments
- Can have different *versions* of the same package

**Benefits of using virtual environments:**

- It prevents package version conflicts between projects
- Makes projects more portable and reproducible
- Keeps your system Python installation clean
- Allows testing with different Python versions

## Create a VirtualEnv

<span class="env-green">**Create**</span> a virtual environment named `myfirstproject`:

```bash
conda create --name myfirstproject python=3.11 -y
```

- `--name` or `-n` specifies the name of the virtual environment. 
- `python=3.11` specifies the Python version to install in the virtual environment. 
- `--yes` or `-y` flag automatically *confirms* the installation without prompting you.

This creates `myfirstproject` environment in <span class="env-green">`~/anaconda3/envs/`</span> with Python 3.11 installed.
You can specify default packages in <span class="env-green">`~/.condarc`</span>.


This is how my `~/.condarc` looks like:

```yaml
# Preferred channel order
channels:
  - https://conda.anaconda.org/conda-forge/
  - defaults
create_default_packages:
  - pip
  - ipython
  - numpy
  - pandas
# Customize the prompt
env_prompt: '({name}) '
changeps1: false
# Disable auto-activation of the base environment
auto_activate_base: false
```

Note that `conda create` is <span class="env-orange">slow</span> as it installs many dependencies. If you want a faster way to create a virtual environment, you can use the <span class="env-green">built-in `venv` module</span> in Python:

```bash
# Create virtual environment with venv
python -m venv .venv

# Activate the virtual environment
source .venv/bin/activate

# Install packages
pip install numpy pandas statsmodels duckdb
```

> If you are unsure, start with `venv` as it is lightweight and part of the standard library. 

With `venv`, no packages will be installed in the virtual environment by default, except for the Python standard library.


|         | `conda`                 | `venv`                 |
| ------- | ----------------------- | ---------------------- |
| Pros    | - Handles system dependencies<br> - Cross-language support<br> - Suitable for ML/geospatial stacks<br> - Support installing pkgs using both `conda` and `pip` later on | - Lightweight<br> - Standard Python tool |
| Cons    | - Heavy and slow<br>    | - Limited to `pip` installing pkgs |


Which tool to use:

- `conda`: when you need non-Python binaries, e.g., R, GDAL, etc
- `venv`: pure Python projects

--------------------------------------------------------------------------------

<span class="env-green">Check the list of virtual environments:</span>

```bash
conda info --envs
# or
conda info -e
```

--------------------------------------------------------------------------------

<span class="env-green">**Activate**</span> the virtual environment using the name:

```bash
conda activate myfirstproject
```

Activating an environment means that all environment actions you perform from the activation moment onward will be performed on the active environment.

The command line will look like this after activation:

```bash
(myfirstproject) ...$
```

Activate a virtual environment `/Users/menghan/anaconda3` using path:

```bash
conda activate /Users/menghan/anaconda3
```

--------------------------------------------------------------------------------

Check **Python executable path** in the virtual environment:

```bash
which python
```

Check the **Python version** in the virtual environment:

```bash
/Users/menghan/anaconda3/envs/myfirstproject/bin/python --version
```

--------------------------------------------------------------------------------

## Install Packages in VirtualEnv

Install packages, e.g., `pandas` in the virtual environment:

```bash
# Make sure you activate the virtual environment first
conda activate myfirstproject
```

```bash
# Install with conda
conda install pandas
```

The package will be installed in the virtual environment. 
You can check the installed packages in the virtual environment by running:

```bash
conda list
```

Check the path of the directory where the package is installed:

```python
>>> import pandas
>>> print(pandas.__file__)
~/anaconda3/envs/myfirstproject/lib/python3.11/site-packages/pandas/__init__.py
```

Alternatively, you can use `pip` to install packages in the virtual environment:

```bash
# Activate the virtual environment first
conda activate myfirstproject

# Install with pip
pip install pandas
```

> `pip` is more complete, while `conda` is more robust in handling dependencies. 


To install multiple packages at once, with specific versions:

```bash
conda install pandas==2.0.3 numpy==2.0.0
```

**conda channels**

The software repositories from conda are called channels. A channel is like a folder and it contains multiple libraries.

- `anaconda`: default channel
- `conda-forge`: community-driven channel with the latest version of libraries.  



--------------------------------------------------------------------------------

**Deactivate** the virtual environment:

```bash
conda deactivate
```

When you deactivate the env, the previously active environment will show, e.g., `(base)`, which is the default environment of Conda.

You must be very careful activating environments and always **must remember to deactivate an environment once you are not going to use it because environments can be stacked**. It means that you can activate an environment on top of another environment. This behavior (which is useful in very specific situations) will lead to chaos in a short amount of time: the libraries installed in the environments will be mixed and you will have no idea where they are installed.



ref:

- [The definitive guide to Python virtual environments with conda](https://www.whiteboxml.com/blog/the-definitive-guide-to-python-virtual-environments-with-conda) 