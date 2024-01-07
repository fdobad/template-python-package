#!python3
""" 👋🌎 This is the package docstring located on `src/bad_mod/__init__.py` """
__author__ = "Fernando Badilla Veliz"
__version__ = 'v0.0.1-1-gaded429-dirty'

import logging

logger = logging.getLogger(__name__)

logger.debug("Importing bad_mod version %s", __version__)
