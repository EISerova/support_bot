import logging

from logging.handlers import RotatingFileHandler

LOGGING_LEVEL = logging.INFO

log = logging.getLogger()
log.setLevel(LOGGING_LEVEL)
formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s - %(funcName)s - %(lineno)d"
)
file_handler = RotatingFileHandler(
    __file__ + ".log", maxBytes=50000000, backupCount=5
)
stream_heandler = logging.StreamHandler()
file_handler.setFormatter(formatter)
stream_heandler.setFormatter(formatter)
log.addHandler(file_handler)
log.addHandler(stream_heandler)