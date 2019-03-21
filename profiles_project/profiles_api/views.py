from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    def get(self,request,format=None):
        """Returns a list of APIView features."""

        an_apiview=[
            'Uses HTTP methods as function',
            'It is similar to traditional Django View'
        ]


        return Response({'message':'Hello!','an_apiview':an_apiview})