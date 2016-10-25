"""
Logging utils
"""

import os
import json
import math
import logging
import configparser
from logging.config import dictConfig


__author__ = 'robodasha'
__email__ = 'damirah@live.com'


def setup_logging(default_path='logging.json', default_level=logging.DEBUG):
    """
    Setup logging configuration
    :param default_path:
    :param default_level:
    :return: None
    """
    path = default_path
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')
    if os.path.exists(path):
        with open(path, 'rt') as f:
            logging_config = json.load(f)
        logging_config['handlers']['file']['filename'] = \
            os.path.join(cfg['paths']['log'], 'debug.log')
        dictConfig(logging_config)
    logging.basicConfig(level=default_level)
    return


def how_often(total, update_freq=100):
    """
    Returns a number indicating after how many processed items should progress
    be printed
    :param total: how many items in total have to be processed
    :param update_freq: default is 100, that is -- update every 1%
    :return: number denoting after how many items should progress be updated
    """
    return math.ceil(float(total) / float(update_freq))


def get_progress(processed, total):
    """
    Based on how many items were processed and how many items are there in total
    return string representing progress (e.g. "Progress: 54%")
    :param processed: number of already processed items
    :param total: total number of items to be processed
    :return: string with current progress
    """
    progress = float(processed) / float(total) * 100
    return "Progress: %.2f%%" % round(progress, 2)
