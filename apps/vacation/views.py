from apps.vacation.models.vacactioncalendar import VacationCalendar
from rest_framework import viewsets, mixins
from .models import Vacation
from .serializers import VacationModelSerializer, VacationCalendarModelSerializer
from rest_framework.permissions import IsAdminUser  # Puedes ajustar los permisos según tus necesidades

class VacationViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    """
        Vacation view set.

        Handle CRUD of Vacation.
    """

    queryset = Vacation.objects.all()
    serializer_class = VacationModelSerializer
    # permissions = [IsAdminUser]


class VacationCalendarViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    """
        Vacation view set.

        Handle CRUD of Vacation.
    """

    queryset = VacationCalendar.objects.all()
    serializer_class = VacationCalendarModelSerializer
    # permissions = [IsAdminUser]