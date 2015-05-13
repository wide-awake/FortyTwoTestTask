from swampdragon.serializers.model_serializer import ModelSerializer


class HttpRequestSerializer(ModelSerializer):
    class Meta:
        model = 'activity.HttpRequest'
        publish_fields = (
            'date_formated',
            'method',
            'server_protocol',
            'status_code',
            'url',
            'content_len',
            'overall'
        )