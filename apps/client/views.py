# from django.shortcuts import render

# Create your views here.
# Django REST Framework
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)

# Serializers
from apps.client import serializers

# My Models
from apps.client.models import Client

class ClientViewSet(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):

    """
        Client view set.

        Handle CRUD of Client.
    """

    queryset = Client.objects.all()
    serializer_class = serializers.ClientModelSerializer
    # permissions = [IsAdminUser]