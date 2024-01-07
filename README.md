![manual workflow](https://github.com/fdobad/template-python-package/actions/workflows/manual.yml/badge.svg)
![auto workflow](https://github.com/fdobad/template-python-package/actions/workflows/auto.yml/badge.svg)
<a href=https://github.com/psf/black>![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)</a>

# A template python package
## Features

* [pyproject.toml][pyproject_config] project configuration
* [Source layout][src-layout] directory structure; project/distribution with 2 packages/modules (w&wo logging)
* [pytest][pytest] framework for functional testing 
* [pdoc3][pdoc3] framework for turning code docstrings to documentation web pages; local `doc/my-repo-name` is published to [`https://user.github.io/my-repo-name`](https://fdobad.github.io/template-python-package)
* Git Hooks:
    - pre-commit auto-updates version in python files
    - pre-push builds documentation web page
* Github workflows:
    - auto.yml : builds & publish documentation web page
    - manual.yml : publish documentation web page

## Usage
* Python script
```python
from fdo_mod import fdo_module
fdo_module.main(['2023','1'])
```
* CLI
```bash
python -m fdo_mod.fdo_module 2023 1
python -m bad_mod -h
```
* Python script that setups its logger 
```python
import bad_mod
logger.getLogger('bad_mod').setLevel(logging.INFO)
TODO
```
## Installation
A. Latest default branch head
```bash
pip install git+https://github.com/user/repo.git
```
B. Specific version
```bash
pip install git+https://github.com/user/repo.git@SUFFIX
    # SUFFIX CAN BE:
    tip of branch:      @branch
    specific commit:    @commit_id  (40 digits long SHA-hash not 7)
    tag (not dirty):    @tag
    ...
    pkg: @[tag|branch]#egg=mypackage
    faster: pip install https://github.com/user/repository/archive/branch.[zip|wheel]
```
C. Line in pip requirements.txt:
```
my-project-name @ git+https://github.com/user/repo.git@SUFFIX
```
## developer  
* editable install (select hooks and yml.actions according to your needs)
```bash
git clone git@git...
cd repo
chmod +x .git/hooks/*
cp hooks/* .git/hooks/.
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.dev.txt
pip install -e .
git checkout -b my_new_feature
# drop -n to execute
git clean -dfX -n
```
* build documentation
```bash
# locally serve a live page of one package/module
pdoc --http localhost:8080 --config latex_math=True fdo_mod
# static files for current directory
pdoc --html --force --output-dir doc --filter=src,tests --config latex_math=True .
```
* run tests
```bash
pytest
```
* forgot where is was?
```bash
$ pip list | grep my-project-name
my-project-name           0.0.0       /home/fdo/source/template-python-package
```
* If a filepath to the local repo is shown and --editable was used: the project can be directly edited & the documentation served live  
* Else from a commit, be sure it is pointing to the correct one on requirements.txt
* Or uninstall and focus on testing

## development tips
### good tips
* Beware of python sessions not reloading the entire packages when `import mypkg`, these should be restarted, not reset.
* Version control tracked files get automatically added to the release, so be tidy, aware of `.gitignore` & beware `git add .`
* Do your feature branch to contribute! `git checkout -b my_new_feature`
* Use docstrings and typed methods to build a great documentation! Even latex (to html or pdf) is available. [more info](https://pdoc3.github.io/pdoc/doc/pdoc/#what-objects-are-documented).
* All new `.py` files should have at least `version` & `author` in the header, sample:
```python
#!python3
""" 
this text is the header module docstring
"""
__author__ = "Software Authors Name"
__copyright__ = "Copyright (C) 1 May 1886 Author Name"
__license__ = "https://anticapitalist.software"
__version__ = "v0.0.1"
```
* pdoc serve many modules
```bash
pip install --editable .
pdoc --http localhost:8080 --config latex_math=True mypkg
pdoc --http localhost:8081 --config latex_math=True otherpkg
```
### ugly tips
* ignore hooks permissions
```bash
git config advice.ignoredHook false
```
* uninstall project before testing
```bash
pip uninstall my-project-name
pytest
```
* just build
```bash
# just in case upgrade build tool
python -m pip install --upgrade build
# creates dist folder with .whl & tar.gz
python -m build
```
* Build files are not automatically cleaned!
```bash
# check first -n is --dry-run
git clean -dfX -n
# once sure, delete them
git clean -dfX
```

## github actions
There're two actions (in .github/workflow) to build the docs webpage:

* manual(lly): publish the webpage action; use `pre-push` hook to build the docs before pushing
* auto: builds & publish the docs online; needs updated requirements.txt & pyproject.toml:dependencies, setup to main-branch pushes only

## git tagging
```bash
# list tags
git tag

# tag current branch-commit
git tag -a v0.0.2 -m "message"

# delete 
## local
git tag --delete v0.0.2
## remote
git push --delete origin v0.0.2

# push 
## a tag
git push origin v0.0.2
## all tags
git push origin --tags
```

# References
* [learn about pytest][pytest]
* [official userguide pyproject config at pypa][pyproject_config]  
* [src project layout][src-layout]  
* [auto publish documentation][auto-publish-docs]  
* [add command line scripts][cli-scripts]  
* [auto python documentation][pdoc3]  
* [advanced pdoc](https://github.com/pdoc3/pdoc/blob/master/pdoc/templates/config.mako)

# Code of Conduct

Everyone interacting in the project's codebases, issue trackers,
chat rooms, and fora is expected to follow the
[PSF Code of Conduct](https://www.python.org/psf/conduct/)_.

[pyproject_config]: https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
[src-layout]: https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout
[cli-scripts]: https://setuptools.pypa.io/en/latest/userguide/entry_point.html
[pdoc3]: https://pdoc3.github.io/pdoc
[auto-publish-docs]: https://github.com/mitmproxy/pdoc/blob/main/.github/workflows/docs.yml
[pytest]: https://docs.pytest.org/en/latest/getting-started.html
