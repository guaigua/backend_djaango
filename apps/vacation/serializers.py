# Django REST Framework
from apps.vacation.models.vacactioncalendar import VacationCalendar
from rest_framework import serializers

# Models
from apps.vacation.models import Vacation

class VacationModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vacation
        fields = "__all__"

class VacationCalendarModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacationCalendar
        fields = "__all__"
