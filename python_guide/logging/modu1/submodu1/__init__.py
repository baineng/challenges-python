import logging

logger = logging.getLogger(__name__)

logger.warning('logging warn in module %s with __name__ %s', 'submodu1',
               __name__)
logger.info('logging info in module %s with __name__ %s', 'submodu1', __name__)
logger.debug('logging debug in module %s with __name__ %s', 'submodu1',
             __name__)

from .. import submodu2
from ..submodu2 import subsubmodu2
