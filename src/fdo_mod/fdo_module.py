#!python3
"""👋🌎
This is the fdo_module docstring
"""
__author__ = "Fernando Badilla"

import logging
import sys
from argparse import ArgumentParser

import numpy as np

logger = logging.getLogger(__name__)


def surround_year_month(y: int, m: int):
    """get previous, current and next month and year in a list of tuples"""
    logger.debug("y: %s, m: %s", y, m)
    nextm = (m % 12) + 1
    prevm = ((m - 2) % 12) + 1
    nexty = y if m < 12 else y + 1
    prevy = y if m > 1 else y - 1
    logger.debug("end")
    return [(prevy, prevm), (y, m), (nexty, nextm)]


def parse_args(argv):
    """Parse command line arguments"""
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase verbosity of output.")
    parser.add_argument("-lf", "--log-filename", default=None, type=str, help="[path]filename for rotating file log.")
    parser.add_argument("input_list", nargs="*", type=int, help="input year and month")
    return parser.parse_args(argv)


def main(argv=None):
    """webscrapping situacion portuaria naves"""
    if argv is None:
        argv = sys.argv[1:]
    args = parse_args(argv)
    from . import SETUP_LOGGER

    SETUP_LOGGER(logger, num_level=args.verbose, filename=args.log_filename)
    logger.info("args %s", args)

    if len(args.input_list) == 0:
        from datetime import date

        today = date.today()
        args.input_list = (today.year, today.month)
        logger.warning("no input list! using today: %s", args.input_list)

    response = surround_year_month(*args.input_list)
    print("previous, current, next (year,month)", response)
    logger.info("previous, current, next (year,month): %s", response)


if __name__ == "__main__":
    sys.exit(main())
