from __future__ import print_function

import os
import logging
import logging.config
from functools import wraps
from datetime import datetime
import pytz

from django.conf import settings


LOGGING = {
    'version': 1,
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': os.path.join(settings.BASE_DIR, 'debug.log'),
        }
    },
    'root': {
        'handlers': ['file'],
        'level': 'DEBUG'
    }
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)


modellog = \
    lambda i: logger.debug([(k, v) for k, v in i.__dict__.iteritems()
                            if not k.startswith("_")])


# TODO: Consider CVB logging mixin
def log_me(func):
    """
    Decorator for logging request data
    """
    @wraps(func)
    def decorator(*args, **kwargs):
        # request object is the first arg in classic django views
        request = args[0]
        logger.info("[{}] path: {}, GET: {}, POST: {}".format(
            datetime.now(pytz.timezone(settings.TIME_ZONE)),
            request.path,
            request.GET,
            request.POST))
        r = func(*args, **kwargs)
        return r

    return decorator
