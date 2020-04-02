# -*- coding: utf-8 -*-

from os import path
import logging
from logging.config import fileConfig

fileConfig(f'{path.abspath(path.dirname(__file__))}/logging_config.conf')
logger = logging.getLogger()

logger.warning('logging warn in %s with __name__ %s', 'root', __name__)
logger.info('logging info in %s with __name__ %s', 'root', __name__)
logger.debug('logging debug in %s with __name__ %s', 'root', __name__)

import modu1
from modu1 import submodu1
