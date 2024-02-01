# Django REST Framework
from rest_framework import serializers

# Models
from apps.company.models import Company

class CompanyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = "__all__"
