from django.shortcuts import render
from .models import Url
from .serializers import UrlSerializer
from rest_framework.views import APIView

# Create your views here.


class PostApiView(APIView):
    def post(self, request):
        data = request.data
        long_url = data.get("url")
        new_url = Url(key="", long_url=long_url, short_url="")
