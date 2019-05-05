from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
class api_views(APIView):
    """docstring forAPIView."""

    serializer_class = serializers.apiSerializer


    def get(self,request,format=None):
        # returns a list of apiview features
        an_apiview =[
            'something something',
            'secondd something',
        ]
        return Response({'message':'it worked','apiview': an_apiview})
