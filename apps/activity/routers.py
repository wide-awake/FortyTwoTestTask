from swampdragon import route_handler
from swampdragon.route_handler import ModelPubRouter

from .serializers import HttpRequestSerializer
from .models import HttpRequest


class HttpRequestRouter(ModelPubRouter):
    serializer_class = HttpRequestSerializer
    model = HttpRequest
    valid_verbs = ['subscribe']
    route_name = 'httprequests'


route_handler.register(HttpRequestRouter)
