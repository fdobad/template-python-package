#!python3
""" 👋🌎
This is the package docstring
"""
__author__ = "Fernando Badilla"
__version__ = 'v0.0.1-0-ge855bdb-dirty'

import logging

logger = logging.getLogger(__name__)

MODULE_WIDE_CONSTANT = 42
""" this is a variable docstring """


def SETUP_LOGGER(logger, num_level=0, filename=None):
    # set the logging level
    if num_level == 0:
        level = logging.WARNING
    elif num_level == 1:
        level = logging.INFO
    elif num_level >= 2:
        level = logging.DEBUG
    logger.setLevel(level)

    # Create a rotating file handler
    if filename:
        from logging.handlers import RotatingFileHandler

        rf_handler = RotatingFileHandler(filename, maxBytes=25 * 1024 * 1024, backupCount=5)
        rf_handler.setLevel(logging.DEBUG)

    # Create a stream handler
    from sys import stdout

    stream_handler = logging.StreamHandler(stdout)
    stream_handler.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s:%(lineno)d %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Add the formatter to the handlers
    stream_handler.setFormatter(formatter)
    if filename:
        rf_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(stream_handler)
    if filename:
        logger.addHandler(rf_handler)
    stream_handler.setLevel(logging.DEBUG)

    # test log
    logger.critical("logger level set to: %s", logging.getLevelName(logger.getEffectiveLevel()))
    logger.debug("test debug")
    logger.info("test info")
    logger.warning("test warning")
    logger.error("test error")
    logger.critical("test critical")
