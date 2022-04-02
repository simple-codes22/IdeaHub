from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Idea
from .serializer import IdeaSerializer, UserSerializer
from rest_framework import generics, mixins, permissions

class UserApiView(
            generics.GenericAPIView,
            mixins.ListModelMixin,
            mixins.CreateModelMixin,
        ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserDetail(
            generics.GenericAPIView,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin
        ):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class IdeaApiView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
    ):
    """API View for the Idea Model"""
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class IdeaDetail(
            generics.GenericAPIView,
            mixins.RetrieveModelMixin,
            mixins.UpdateModelMixin,
            mixins.DestroyModelMixin
        ):
    queryset = Idea.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
