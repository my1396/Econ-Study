---
layout: post
tag: programming
title: Python Config
---

<a class="top-link hide" href="#" id="js-top">↑</a>

## Install packages

Use `which -a`  to see all python executables.



**Conda Commands**

<https://docs.conda.io/projects/conda/en/stable/commands/init.html>

`conda init ` will add your conda executable file in your `$PATH` variable.

`conda init [SHELLS]`  Available shells: ['bash', 'fish', 'powershell', 'tcsh', 'xonsh', 'zsh']. One or more shells to be initialized. If not given, the default value is <span style='color:#00CC66'>'bash' on unix</span> and 'cmd.exe' & 'powershell' on Windows. 

On Mac, when you install Anaconda or Miniconda, `.bash_profile` gets updated with the following code:

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/menghan/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/menghan/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/menghan/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/menghan/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<
```

Issue: The result of default `conda init` is that the environment variable is inserted in `.bash_profile` even if `zsh` is your default shell.

Fix: You need to specify explicitly <span style='color:#00CC66'>the shell to be `zsh`</span>. Run `conda init zsh` will add the same code to `.zshrc`.



`conda info` display info about current conda install.



`conda env list` list all conda environments.

**Determine your current env**

By default, the active environment---the one you are currently using---is shown in parentheses () or brackets [] at the beginning of your command prompt:

```bash
(myenv) $
```

If you do not see this, run:

```bash
conda info --envs # list all envs, the active one is prefixed w/ *
```

In the environments list that displays, your current environment is highlighted with an asterisk (`*`).



To see **if a specific package is installed** in an environment:

```bash
conda list --name myenv scipy # full flag
conda list -n myenv scipy # same cmd but in shorthand
conda list scipy # check in the current-active env

conda list # print all installed packages
conda list -n myenv # print all installed packages in myenv
```



### `conda install`

arguments:

- `-n, --name` specify name of environment
- `-p, --prefix` full path to environment location
- `-c, --channel` Additional channel to search for packages.
- a list of packages can be installed at once. Jist append pkgs together and separate by space.

Examples:

- Install the package 'scipy' into the currently-active environment:
  ```bash
  conda install scipy
  ```

- Install a list of packages into an environment, `myenv`:
  ```bash
  conda install -n myenv scipy curl wheel
  ```

- Install a specific version of 'python' into an environment, `myenv`:
  ```bash
  conda install -p path/to/myenv python=3.11
  ```



`conda search` Search packages in the default `channel_alias`  https://conda.anaconda.org/. Can specify additional channel using `conda search conda-forge::[some package name]`.

- search for a specific package named 'scikit-learn':
  ```bash
  conda search scikit-learn
  ```

- Search for packages containing 'scikit' in the package name:
  ```bash
  conda search *scikit* # [✘]
  ```
  - Note that your shell may expand '*' before handing the command over to conda. Therefore, it is sometimes necessary to use single or double quotes around the query:
    ```bash
    conda search '*scikit' # [✔]
    conda search "*scikit*" # [✔]
    ```

- Search for a specific version of a package:
  ```bash
  conda search 'numpy>=1.12'
  ```

- Search for a package on a specific channel `conda-forge`:
  ```bash
  conda search conda-forge::numpy
  conda search 'numpy[channel=conda-forge, subdir=osx-64]'
  ```



### Install packages from Anaconda.org

1. In a browser, go to [http://anaconda.org](http://anaconda.org/).
2. To find the package named *PyPortfolioOpt*, type `PyPortfolioOpt` in the top-left box named Search Packages.
3. Follow the instructions in the detailed page.



### Using `pip`

```bash
conda install -n myenv pip
conda activate myenv
pip <pip_subcommand>
```

Note: Issues may arise when using `pip` and `conda` together. 

- When combining `conda` and `pip`, it is best to use an isolated conda environment. 
- Only after `conda` has been used to install as many packages as possible, should `pip` be used to install any remaining software.



`python -m pip`  executes pip using the Python interpreter you specified as python. 

- So `/usr/bin/python3.7 -m pip` means you are executing pip for your interpreter located at `/usr/bin/python3.7`.

  ```python
  python -m pip install SomePackage            # latest version, installed in the correct location for the python version you are using
  python -m pip install SomePackage==1.0.4     # specific version
  python -m pip install 'SomePackage>=1.0.4'     # minimum version
  ```

  `python -m module-name` the given module is located on the Python module path and executed as a script. 

  





## Update Python

- Using a different version of Python 

  ```py
  conda activate myenv # activate myenv
  conda update python # update Python to the latest version in the current env
  conda install python=3.10 # update to a specific version of Python
  ```

- Create a new environment for the new Python

  ```bash
  conda create -n py39 python=3.9 # create a new env called py39
  conda activate py39  # activate py39
  python --version # print Python version
  ```




Viewing a list of available Python versions

- To list the versions of Python that are available to install, in your terminal window, run:

  ```python
  conda search python # This lists all packages whose names contain the text `python`.
  ```

- To list only the packages whose full name is exactly `python`, add the `--full-name` option. 

  ```python
  conda search --full-name python
  ```