from rest_framework import serializers
from .models import Url


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ["key", "long_url", "short_url"]
