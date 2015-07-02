import os
import logging

from django.conf import settings


# logging config
logging.basicConfig(disable_existing_loggers=1,
                    filename=os.path.join(settings.BASE_DIR, 'debug.log'),
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)


class FileLoggerMiddleware(object):

    def process_response(self, request, response):
        request_log = 'Path: {}, GET: {}, POST: {}'.format(
            request.path, request.GET, request.POST)
        logger.info(request_log)

        # We have queries logging out of box
        # But here what i wood wrote -
        # http://stackoverflow.com/a/31189558/2576817
        return response
