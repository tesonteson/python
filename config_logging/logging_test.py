import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler("logtest.log")
logger.addHandler(handler)

def do_something():
    logger.info("from logging_test info")
    logger.debug("from logging_test debug")
