from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import  filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import models
from . import serializers
from . import permissions
# Create your views here.

class HelloApiView(APIView):
    """Test API View."""

    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features."""

        an_apiview=[
            'Uses HTTP methods as function',
            'It is similar to traditional Django View'
        ]


        return Response({'message':'Hello!','an_apiview':an_apiview})

    def post(self,request):
        """create a hello with a name."""

        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Updates"""
        return Response({'method':'put'})

    def patch(self,request,pk=None):
        """Patch request,only fields provided"""

        return Response({'method':'patch'})

    def delete(self,request,pk=None):

        return Response({'method':'delete'})

class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""
    serializer_class=serializers.HelloSerializer
    def list(self,request):
        """Return hello msg."""

        a_viewset=[
            'uses actions',
            'Automatically maps to URLS using Routers',
        ]

        return Response({'message':'hello','a_viewset':a_viewset})

    def create(self,request):
        """create a new msg"""

        serializer=serializers.HelloSerializer(data=request.data)

        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format('name')
            return Response({'message':message})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):

       return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})


    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.Userprofile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields=('name','email',)

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and return auth token"""

    serializer_class=AuthTokenSerializer

    def create(self,request):
        return ObtainAuthToken().post(request)

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.PostOwnStatus,IsAuthenticated)

    def perform_create(self,serializer):
        serializer.save(user_profile=self.request.user)

