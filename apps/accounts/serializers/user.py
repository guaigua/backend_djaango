# Django


# Django REST Framework
from rest_framework import serializers


# Models
from apps.accounts.models import User


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

