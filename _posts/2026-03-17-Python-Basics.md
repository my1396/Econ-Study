---
layout: post
tag: python
title: Python Basic Syntax
date: 2026-03-17
---

[Python 3 Documentation](https://docs.python.org/3/index.html)

Python starts index with 0, which means the first element of a list is accessed with index 0.

`type()` to check the data type of a variable.



**For data frames:**

- `df.dtypes` to check the data types of each column in the data frame.

- `df.info()` to check the data types of each column and the number of non-null values. 

- `df.describe()` to get summary statistics of the numerical columns in the data frame.




## Virtural Environment

Python is shipped with the OS out of box for UNIX-based systems. If you run `which python`, you will see sth like `usr/bin/python3`, this is the system Python. It is NOT recommended to install packages in the system Python as it may cause <span class="env-green">conflicts with the OS and other applications that rely on it</span>. 
You might end up with some complicated fixes or fresh OS installation if you mess with the system Python.
Therefore, you should use a virtual environment to manage your project-specific dependencies.


> Rule of thumb: Don't mess with the base environment of Conda or the system Python. Always create a new virtual environment for each project to keep things clean and organized.

A virtual environment in Python is an isolated environment on your computer. It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.




Each virtual environment:

- Has its own Python interpreter
- Has its own set of installed packages
- Is isolated from other virtual environments
- Can have different versions of the same package

Benefits of using virtual environments:

- It prevents package version conflicts between projects
- Makes projects more portable and reproducible
- Keeps your system Python installation clean
- Allows testing with different Python versions

## Create a VirtualEnv

Create a virtual environment named `myfirstproject`:

```bash
conda create -name myfirstproject python=3.11 -y
```

- `--name` or `-n` specifies the name of the virtual environment. 
- `python=3.11` specifies the Python version to install in the virtual environment. 
- `-y` flag automatically confirms the installation without prompting you.

This creates `myfirstproject` environment in `~/anaconda3/envs/` with Python 3.11 installed.
You can specify default packages in `~/.condarc`, 


Note that `conda create` is slow as it installs many dependencies. If you want a faster way to create a virtual environment, you can use the <span class="env-green">built-in `venv` module</span> in Python:

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


```yaml
create_default_packages:
  - numpy
  - pandas
```


Check the list of virtual environments:

```bash
conda info --envs
# or
conda info -e
```


--------------------------------------------------------------------------------

**Activate** the virtual environment:

```bash
conda activate myfirstproject
```

Activating an environment means that all environment actions you perform from the activation moment onward will be performed on the active environment.

The command line will look like this after activation:

```bash
(myfirstproject) ...$
```


Check **Python executable** path in the virtual environment:

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


## Install R in VirtualEnv

You can also install R in a virtual environment.

```bash
# Create a new environment with R
conda create -n r_env r-essentials -y
```

This will create a new environment named `r_env` with R and the essential R packages installed. You can activate this environment and use R within it.

```bash
# Activate the R environment
conda activate r_env
```


ref:

- [The definitive guide to Python virtual environments with conda](https://www.whiteboxml.com/blog/the-definitive-guide-to-python-virtual-environments-with-conda) 