#!python3
"""👋🌎
This is the fdo_module docstring located on `src/fdo_mod/fdo_module.py`

Scripts using this module should import it like this:
```python
from fdo_mod import fdo_module
fdo_module.main()
```
You could import `surround_year_month` directly, but miss the main logic
"""
__author__ = "Fernando Badilla"
__version__ = 'v0.0.1-3-g1db3be4-dirty'

import logging
import sys
from argparse import ArgumentParser

logger = logging.getLogger(__name__)


def surround_year_month(y: int, m: int) -> list[tuple[int, int]]:
    """get previous, current and next month and year in a list of tuples
    Args:
        y (int): year
        m (int): month
    Returns:
        list: [(previous year, previous month), (year, month), (next year, next month)]
    Raises:
        TypeError: if y or m are not integers
        ValueError: if m is not between 1 and 12
    """  # fmt: skip
    if not isinstance(y, int) or not isinstance(m, int):
        raise TypeError("y and m must be integers")
    if not 1 <= m <= 12:
        raise ValueError("m must be between 1 and 12")
    logger.debug("y: %s, m: %s", y, m)
    nextm = (m % 12) + 1
    prevm = ((m - 2) % 12) + 1
    nexty = y if m < 12 else y + 1
    prevy = y if m > 1 else y - 1
    logger.debug("end")
    return [(prevy, prevm), (y, m), (nexty, nextm)]


def parse_args(argv):
    """argument parser (besides -h) only recieves a list of integers, should be 2: year and month"""
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("input_list", nargs="*", type=int, help="input year and month")
    return parser.parse_args(argv)


def main(argv=None):
    """ parses arguments, if argv is None, uses sys.argv[1:],  
    if args still empty, uses today's year and month
    Args:
        argv (list[str] | None): string list arguments, can be None to allow using  
            - sys.argv on command line usage   
            - or calling it from another script or module as fdo_basics.main(["-h"])
    Returns:
        int: 0 if success, 1 if error
    """  # fmt: skip
    if argv is None:
        argv = sys.argv[1:]
    args = parse_args(argv)
    logger.debug("args %s", args)
    logger.warning("logging level is %s", logging.getLevelName(logger.getEffectiveLevel()))

    if len(args.input_list) == 0:
        from datetime import date

        today = date.today()
        args.input_list = (today.year, today.month)
        logger.warning("no input list! using today: %s", args.input_list)

    try:
        response = surround_year_month(*args.input_list)
        print("previous, current, next (year,month)", response)
        return 0
    except Exception as e:
        logger.error("error: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
