from __future__ import print_function

import os
import logging
import logging.config

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
