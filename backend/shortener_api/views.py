from django.shortcuts import render, redirect
from .models import Url
from .serializers import UrlSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.


class PostApiView(APIView):
    def get_object(self, key):
        try:
            return Url.objects.get(key=key)
        except Url.DoesNotExist:
            raise Http404

    def get(self, request, key):
        url = self.get_object(key)
        serializer = UrlSerializer(url)
        return redirect(url.long_url)

    def post(self, request):
        data = request.data
        domain = request.get_host()
        long_url = data.get("url")
        if request.is_secure():
            protocol = "https://"
        else:
            protocol = "http://"
        my_url = {"long_url": long_url}
        key = str(abs(hash(long_url)) % (10 ** 6))
        my_url["key"] = key
        my_url["short_url"] = f"{protocol}{domain}/{key}"
        serializer = UrlSerializer(data=my_url)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
