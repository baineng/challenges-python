# -*- coding: utf-8 -*-

import logging

logging.basicConfig(
    level=logging.INFO,
    format=
    '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s'
)
logger = logging.getLogger()

logger.warning('logging warn in %s with __name__ %s', 'root', __name__)
logger.info('logging info in %s with __name__ %s', 'root', __name__)
logger.debug('logging debug in %s with __name__ %s', 'root', __name__)

import modu1
from modu1 import submodu1
