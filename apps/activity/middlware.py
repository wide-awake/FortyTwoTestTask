from .models import HttpRequest


class ReqCatchMiddleware(object):

    def process_response(self, request, response):
        request_data = HttpRequest(method=request.META['REQUEST_METHOD'],
                                   server_protocol=request.META['SERVER_PROTOCOL'],
                                   status_code=response.status_code,
                                   url=request.path,
                                   content_len=len(response.content))
        request_data.save()
        return response