from swampdragon.serializers.model_serializer import ModelSerializer


class HttpRequestSerializer(ModelSerializer):
    class Meta:
        model = 'activity.HttpRequest'
        publish_fields = ('data', )
        update_fields = ('data', )