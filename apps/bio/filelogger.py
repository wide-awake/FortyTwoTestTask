from __future__ import print_function

import os
import logging
import logging.config
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


model_log = \
    lambda i: logger.debug([(k, v) for k, v in i.__dict__.iteritems()
                            if not k.startswith("_")])

req_log = \
    lambda r: logger.info("[{}] path: {}, GET: {}, POST: {}".format(
        datetime.now(pytz.timezone(settings.TIME_ZONE)),
        r.path,
        r.GET,
        r.POST))
