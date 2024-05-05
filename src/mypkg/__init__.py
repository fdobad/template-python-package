#!python3
"""👋🌎🔥
This is the package docstring
"""
__author__ = "Fernando Badilla"
__revision__ = "$Format:%H$"

import logging
from pathlib import Path

from importlib_metadata import PackageNotFoundError, distribution

logger = logging.getLogger(__name__)

try:
    __version__ = distribution("my-project-name").version
    version_from = "importlib_metadata"
except PackageNotFoundError:
    if (Path(__file__).parent / "_version.py").exists():
        from ._version import __version__

        version_from = "_version.py"
    else:
        __version__ = "0.0.0"
        version_from = "fallback"

logger.warning("%s Package version: %s, from %s", __name__, __version__, version_from)

PACKAGE_WIDE_CONSTANT = 42
""" this is a variable docstring """


def setup_logger(name: str = __name__, verbosity: str = "INFO", logfile: Path | None = None):
    """ Users or developers not implementing their own logger should use this function to get enhanced program execution information.
    Capture the logger, setup its __name__, verbosity, stream handler & rotating logfile.

    Args:
        name (str, optional): Name of the logger. Defaults to \__name __ 
        verbosity (str, optional): Verbosity level, implemented INFO (20, default), WARNING (30) or DEBUG (10, no matches)
        logfile (Path, optional): Create a -rotated- logfile (5 files, 25MB each).
    Returns:
        logger (Logger):  All code in this pkg uses logger.info("..."), logger.debug, etc.

    # Regular Usage Guideline
    logging.critical("Something went wrong, exception info?", exc_info=True)
    logging.error("Something went wrong, but we keep going?")
    logging.warning("Default message level")
    logging.info("Something planned happened")
    logging.debug("Details of the planned thing that happened")
    print("Normal program output, not logged")
    """  # fmt: skip
    import sys

    # Capture the logger
    logger = logging.getLogger(name)
    # Create a stream handler
    stream_handler = logging.StreamHandler(sys.stdout)
    # Create a rotating file handler
    if logfile:
        from logging.handlers import RotatingFileHandler

        rf_handler = RotatingFileHandler(logfile, maxBytes=25 * 1024, backupCount=5)
    # Set the logs level
    match verbosity:
        case "WARNING":
            level = logging.WARNING
        case "INFO":
            level = logging.INFO
        case _:
            level = logging.DEBUG
    logger.setLevel(level)
    stream_handler.setLevel(level)
    if logfile:
        rf_handler.setLevel(level)
    # formatter
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s %(filename)s:%(lineno)d %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    stream_handler.setFormatter(formatter)
    if logfile:
        rf_handler.setFormatter(formatter)
    # Add the handlers to the logger
    logger.addHandler(stream_handler)
    if logfile:
        logger.addHandler(rf_handler)
    logger.warning("Logger initialized @level %s", logging.getLevelName(level))
    return logger
