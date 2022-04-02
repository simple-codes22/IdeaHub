"""
    This is the serializer section which the models would be made available as APIs for frontend External Use
"""
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Idea

class UserSerializer(serializers.ModelSerializer):
    """
        Serializer for the User Model
    """
    class Meta:
        model = User
        fields = '__all__'

class IdeaSerializer(serializers.ModelSerializer):
    """
        Serializer for the Idea Model
    """
    class Meta:
        model = Idea
        fields = '__all__' # It takes all the model fields 