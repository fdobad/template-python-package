#!python3
"""
This is the OTHER PKG package docstring
"""
__author__ = "Fernando Badilla"
__revision__ = "$Format:%H$"

from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # FIXME two pyproject.toml version file ?
    # harcoded version number
    # from ._version import __version__

    # fallback
    __version__ = "0.0.0"

import logging as _logging

_logger = _logging.getLogger(__name__)
_logging.basicConfig(level=_logging.INFO)
_logger.debug("Hello world! from OTHER PKG")

PACKAGE_WIDE_CONSTANT = 66
""" this variable is available to all modules in this other package """
