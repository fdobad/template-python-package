![manual workflow](https://github.com/fdobad/template-python-package/actions/workflows/manual.yml/badge.svg)
![auto workflow](https://github.com/fdobad/template-python-package/actions/workflows/auto.yml/badge.svg)
<a href=https://github.com/psf/black>![Code style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)</a>

_Easy python project template_

# Overview
* A [source layout][src-layout] python project/distribution with 2 packages/modules
* [pyproject.toml][pyproject_config] project configuration file
    - setuptools-scm default versioning
* [pytest][pytest] unit testing
* Code documentation page using pdoc3, publishing pages from `doc/my-repo-name` to [`https://user.github.io/my-repo-name`](https://fdobad.github.io/template-python-package)
* Optional git hooks:
    - To run tests, could be in pre-commit or pre-push 
    - To generate documentation in pre-commit

# Install
Command line interface:
```bash
pip install git+https://github.com/user/repo.git
```
Line in `requirements.txt`
```
my-project-name @ git+https://github.com/user/repo.git
```
Required:  
- A github account with ssh credentials  
- Or deploy credentials  

_PyPI integration (`pip install project-name` comming soon)_

## Specific version install
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
Or as a line in requirements.txt:
```
my-project-name @ git+https://github.com/user/repo.git@SUFFIX
```

# Develop
```bash
# clone
git clone git@github.com:fdobad/template-python-package.git
cd template-python-package

# virtual environment
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.dev.txt

# install in editable mode
pip install --editable . 

# live documentation
pdoc --http localhost:8080 --config latex_math=True mypkg

# choose your hooks (very optional)
cp hooks/* .git/hooks/
chmod +x .git/hooks/*

# feature branch
git checkout -b my_new_feature

# test
pytest

# clean (-n is dry-run, remove to delete)
git clean -dfX -n

# view calculated version
python -m setuptools_scm

# tag
git tag -a v1.2.3 -m 'message'

# build : creates `dist` with .whl & tar.gz files
python -m build
```

## Keep in mind
1. To generate a clean release, make sure `version_file` is commented (writing a version file is useful for tracking dirty versions, but changes that file every time you build, so you'll never get a clean tag)
```
[tool.setuptools_scm]
# version_file = "src/mypkg/_version.py"
```

2. Activate your python venv, check if/where is installed:
```bash
$ pip list | grep my-project-name
my-project-name           0.0.0       /home/fdo/source/template-python-package
```
* If a filepath to the local repo is shown and --editable was used: the project can be directly edited & the documentation served live  
* Else from a commit, make sure it is pointing to the correct version on requirements.txt or the pip command  

3. Beware `import mypkg` is made once per [i]python session; changes will reflect when restarting, not resetting

4. Version control tracked files inside src/pkg get automatically added to the release (be tidy, aware of `.gitignore` & beware `git add .`)

5. Documenting with pdoc3:
    1. `doc` is served by github pages (check `.github/workflows/*yml` for auto or manual configuration)
    2. `doc` can be generated locally or remotely (manual or auto, if using weird dependencies building locally/manual is recommended)
    3. A good practice is updating the web page only when pushing to a specific branch (like `doc`)
    4. `doc` is added to .gitignore to avoid the clutter (useful when autogenerating with the pre-commit hook that only works on the `doc` branch). remove it or use `git add -f doc` to force adding it to the repo.
    5. Docstrings support latex (also to html or pdf) is available. [more info](https://pdoc3.github.io/pdoc/doc/pdoc/#what-objects-are-documented). 

6. Type hints are not enforced, but are a good practice. [more info](https://docs.python.org/3/library/typing.html)

7. Minimal documentation should include: Module, global_variables, classes, methods docstrings. A good descriptive sentence (with and example) is better than a long paragraph of Arguments, Returns & Raises that Copilot can generate.

8. TODO: Docstring examples are not tested! 
    
9. New python files should have at least the following header:
```python
#!python3
""" 
this text is the header module docstring
"""
__author__ = "Software Authors Name"
__date__ = "2024-05-01"
__copyright__ = "Copyleft (C) 1 May 1886 Author Name"
__license__ = "https://anticapitalist.software"
__revision__ = "$Format:%H$"
```

### pdoc samples
```bash
pdoc --html --force --output-dir doc .
pdoc --html --http : --force --output-dir doc --config latex_math=True .
pdoc --html --http localhost:8080 --force --output-dir doc mypkg
```
other examples at hooks/pre-commit
https://github.com/pdoc3/pdoc/blob/master/pdoc/templates/config.mako

### git tag(ging)
Semantic versioning[semantic-versioning]: The idea of semantic versioning (or SemVer) is to use 3-part version numbers, major.minor.patch, where the project author increments:

    major when they make incompatible API changes,
    minor when they add functionality in a backwards-compatible manner, and
    patch, when they make backwards-compatible bug fixes.

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
* [auto python documentation][auto-document]  
* [auto publish documentation][auto-publish-docs]  
* [add command line scripts][cli-scripts]  

# Code of Conduct

Everyone interacting in the project's codebases, issue trackers,
chat rooms, and fora is expected to follow the
[PSF Code of Conduct](https://www.python.org/psf/conduct/)_.

[pyproject_config]: https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html
[src-layout]: https://setuptools.pypa.io/en/latest/userguide/package_discovery.html#src-layout
[cli-scripts]: https://setuptools.pypa.io/en/latest/userguide/entry_point.html
[auto-document]: https://pdoc3.github.io/pdoc
[auto-publish-docs]: https://github.com/mitmproxy/pdoc/blob/main/.github/workflows/docs.yml
[pytest]: https://docs.pytest.org/en/latest/getting-started.html
[semantic-versioning]: https://packaging.python.org/en/latest/discussions/versioning/#valid-version-numbers
