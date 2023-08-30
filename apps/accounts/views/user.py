# Django REST Framework
from unittest import result
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser
)

# Serializers
from apps.accounts import serializers

# My Models
from apps.accounts.models import User

# Utils



class UserViewSet(mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    """
        User view set.

        Handle sign up, login and account verification.
    """
    filter_backends = ( DjangoFilterBackend,)
    filterset_fields  = ["is_active"] 

    queryset = User.objects.all()
    serializer_class = serializers.UserModelSerializer

    def get_permissions(self):
        """Assign permissions based on action."""
        print(self.action)
        if self.action in ['login','check','retrieve','change_password']:
            permissions = [AllowAny]
        elif self.action in ['logout']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAdminUser]
        return [p() for p in permissions]
    
    def get_serializer_class(self):
        """Return serializer based on action."""

        return serializers.UserModelSerializer

    # Def to update a employee
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        serializer = serializers.UserModelSerializer(instance,many=False).data

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer)

    # Def to delete a user
    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()