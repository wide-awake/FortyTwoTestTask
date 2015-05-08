from swampdragon import route_handler
from swampdragon.route_handler import ModelPublisherRouter

from .serializers import HttpRequestSerializer
from .models import HttpRequest


class HttpRequestRouter(ModelPublisherRouter):
    serializer_class = HttpRequestSerializer
    model = HttpRequest
    route_name = 'http_requests'

    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    def get_query_set(self, **kwargs):
        return self.model.all()


route_handler.register(HttpRequestRouter)
