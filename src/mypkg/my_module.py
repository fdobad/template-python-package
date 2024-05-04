#!python3
"""👋🌎🔥
This is the mypkg my_module docstring
"""
__author__ = "Fernando Badilla"
__version__ = "v0.0.1+4-gc984bd5-dirty"

import logging
import sys

import numpy as np

from . import PACKAGE_WIDE_CONSTANT

logger = logging.getLogger(__name__)


def my_function(x: int = PACKAGE_WIDE_CONSTANT):
    """ This function has latex documentation:
    $$
    \mathcal{O}(N) \\
    X = \$3.25
    $$

    Blocks of math delimited with 'brackets' style are supported and should stay so:
    \[
    \mathcal{O}(N) \\
    X = \$3.25
    \]
    """
    logger.info("Hi, Mom!")
    return x + np.random.rand()


def my_other_function(x: int = 0):
    """This function has latex documentation
    $$
    \mathbb{H} \in \lambda \lambda  \sigma
    $$
    inline also?
    """
    logger.info("Hi, Dad!")
    return x + np.random.randint(1 + int(x))


def my_third_function(x: int = 0, y: int = 0):
    """Αυτό είναι ελληνικό κείμενο."""
    return x + y + np.random.randint(1 + int(x + y))


def my_documented_function(*args, **kwargs) -> bool:
    """Do important stuff.

    More detailed info here, in separate paragraphs from the subject line.
    Use proper sentences -- start sentences with capital letters and end
    with periods.

    Can include annotated documentation:

    :param short_arg: An argument which determines stuff.
    :param long_arg:
        A long explanation which spans multiple lines, overflows
        like this.
    :returns: The result.
    :raises ValueError:
        Detailed information when this can happen.

    .. versionadded:: 6.0
    """
    logger.debug(f"Hi, docs! {args} {kwargs}")
    return True


def morefunc(x: int = 0):
    return x**2 + 33


def jalisco_nunca_pierde(numbers: list):
    """Jalisco nunca pierde is slang for a 1937 movie "Jalisco never loses"."""
    if not isinstance(numbers, list):
        numbers = [numbers]
    tmp = []
    for num in numbers:
        try:
            tmp += [float(num)]
        except ValueError:
            pass
    retval = np.array(tmp).sum() + 1
    logger.info("Jalisco wins with: %s,", retval)
    return retval


def arg_parser(argv):
    import argparse

    parser = argparse.ArgumentParser(description="This is a sample program.")
    parser.add_argument("numbers", nargs="*", help="List of numbers")
    parser.add_argument("--verbose", "-v", action="count", default=0)
    return parser.parse_args(argv)


def main(argv=None):
    """Main can be run from command line or import it passing a list as sys.argv.
    On cli calls, it should return a status code: 0 for success, >=1 for failure(s).
    On scripting calls, an argument can modify this behavior.
    """
    if argv is None:
        argv = sys.argv
    argv = argv[1:]
    args = arg_parser(argv)
    print(args)
    if args.verbose != 0:
        global logger
        from mypkg import setup_logger

        match args.verbose:
            case 1:
                logger = setup_logger(verbosity="WARNING")
            case 2:
                logger = setup_logger(verbosity="INFO")
            case _:
                logger = setup_logger(verbosity="DEBUG")

    win = jalisco_nunca_pierde(args.numbers)
    return 0
    if len(argv) > 1:
        num = int(argv[1])
        logger.info(f"Hello, {num}!")
        print(my_function(num))


if __name__ == "__main__":
    sys.exit(main(sys.argv))
