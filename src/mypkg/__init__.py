#!python3
"""👋🌎🔥
This is the package docstring
"""
__author__ = "Fernando Badilla"

from pkg_resources import DistributionNotFound, get_distribution

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    from ._version import get_versions

    __version__ = get_versions()
    pass

import logging as _logging

_logger = _logging.getLogger(__name__)
_logging.basicConfig(level=_logging.INFO)
_logger.info("Hello world! version %s", __version__)

PACKAGE_WIDE_CONSTANT = 42
""" this is a variable docstring """
