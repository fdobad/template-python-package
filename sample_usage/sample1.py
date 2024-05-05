#!python3

from mypkg import setup_logger
from mypkg.my_module import jalisco_nunca_pierde

logger = setup_logger(verbosity="DEBUG", logfile="jalisco.log")

logger.info("Hello World!, Starting the program")
challenge = 3
logger.info("Challenge is %s", challenge)
logger.info("Jalisco wins with: %s", jalisco_nunca_pierde(challenge))
logger.info("Bye world!")
