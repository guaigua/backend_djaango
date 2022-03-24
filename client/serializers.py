# Django
from django.core.validators import RegexValidator

# Django REST Framework
from rest_framework import serializers

# Models
from client.models import Clients

class ClientModelSerializer(serializers.ModelSerializer):

    class Meta:

        model = Clients
        fields = "__all__"

class ShortClientModelSerializer(serializers.ModelSerializer):

    class Meta:

        model =  Clients
        fields = ["username"]