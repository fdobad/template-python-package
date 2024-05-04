#!python3
"""👋🌎🔥
This is the mypkg my_module docstring
"""
__author__ = "Fernando Badilla"
__version__ = "v0.0.1+4-gc984bd5-dirty"

import logging
import sys

import numpy as np

from mypkg import PACKAGE_WIDE_CONSTANT

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


def jalisco_nunca_pierde(challenge: float | int = 0):
    """Jalisco nunca pierde is slang for a 1937 movie "Jalisco never loses". This function sums the input and adds 1 to win!

    Args:
        challenge (float | int, optional): challenge number. Defaults to 0.
    Returns:
        float | int: challenge + 1 winning!
    Raises:
        ValueError: If numbers is not a list.
    """
    if not isinstance(challenge, (float, int)):
        raise ValueError("challenge is not a (float or int) number")
    retval = challenge + 1
    logger.info("Jalisco wins with: %s,", retval)
    return retval


def arg_parser(argv):
    import argparse

    parser = argparse.ArgumentParser(description="This is a sample program.")
    parser.add_argument("number", nargs="?", help="number to challenge Jalisco.")
    parser.add_argument("--verbose", "-v", action="count", default=0)
    parser.add_argument(
        "--retval",
        "-r",
        action="store_true",
        help="Return value from main instead of return code. Useful for integrating main into other scripts.",
    )
    return parser.parse_args(argv)


def main(argv=None):
    """Main can be run from command line or import it passing a list as sys.argv.
    On cli calls, it should return a status code: 0 for success, >=1 for failure(s).
    On scripting calls, an argument can modify this behavior.

    args = arg_parser(None)
    """
    if argv is sys.argv:
        argv = sys.argv[1:]
    args = arg_parser(argv)
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

    try:
        win = jalisco_nunca_pierde(float(args.number))
        print("jalisco won with:", win)
        if args.retval:
            return win
        return 0
    except Exception as e:
        logger.error("Error: %s", e, exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
