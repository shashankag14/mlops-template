# mlops-template
A simple and flexible project template for MLOps.


## Building the model package
To generate the distribution package for the model, we use [PyPA](https://packaging.python.org/en/latest/). It would create a versioned archive file that contains Python packages, modules, and other resource files that are used to distribute a release. Later, this distribution package could be installed via `pip` to import it as a module.

#### Steps to build the model package:
##### 1. Make sure you have the latest version of PyPA’s build installed:

```http
  python3 -m pip install --upgrade build  # for Unix/macOS
  py -m pip install --upgrade build     # for Windows
```

##### 2. Run this command from the same directory where `pyproject.toml` is located:

```http
  python3 -m build  # for Unix/macOS
  py -m build     # for Windows
```

