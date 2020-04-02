# -*- coding: utf-8 -*-

from os import path
import logging
from logging.config import dictConfig

logging_config = dict(
    version=1,
    formatters={
        'f': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    handlers={
        'h': {
            'class': 'logging.StreamHandler',
            'formatter': 'f',
            'level': logging.DEBUG
        }
    },
    root={
        'handlers': ['h'],
        'level': logging.INFO,
    })
dictConfig(logging_config)

logger = logging.getLogger()
logger.warning('logging warn in %s with __name__ %s', 'root', __name__)
logger.info('logging info in %s with __name__ %s', 'root', __name__)
logger.debug('logging debug in %s with __name__ %s', 'root', __name__)

import modu1
from modu1 import submodu1
