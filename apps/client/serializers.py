# Django
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers

# Models
from apps.client.models import Client

class ClientModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Client
        fields = "__all__"

class ShortClientModelSerializer(serializers.ModelSerializer):

    class Meta:

        model =  Client
        fields = ["username"]