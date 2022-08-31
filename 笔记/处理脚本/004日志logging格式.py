import logging
from logging.handlers import RotatingFileHandler
import os



def log_config():
    abs_path = os.path.dirname(os.path.abspath(__file__))
    logging.basicConfig(level=logging.DEBUG)
    log_path = os.path.join(abs_path, 'flask.log')
    file_log_handler = RotatingFileHandler(log_path, encoding='UTF-8', maxBytes=1024*1024*100, backupCount=100)
    # formatter = logging.Formatter("%(levelname)s %(asctime)s [%(filename)s]: %(lineno)s - %(funcName)s - %(message)s")
    formatter = logging.Formatter("%(levelname)s %(asctime)s [%(funcName)s] =====> [%(message)s]")
    file_log_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_log_handler)
    return logging