import logging

logger = logging.getLogger(__name__)

logger.warning('logging warn in module %s with __name__ %s', 'subsubmodu2',
               __name__)
logger.info('logging info in module %s with __name__ %s', 'subsubmodu2',
            __name__)
logger.debug('logging debug in module %s with __name__ %s', 'subsubmodu2',
             __name__)
