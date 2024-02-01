from rest_framework import viewsets, mixins
from .models import Company
from .serializers import CompanyModelSerializer
from rest_framework.permissions import IsAdminUser  # Puedes ajustar los permisos según tus necesidades

class CompanyViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):

    """
        Company view set.

        Handle CRUD of Company.
    """

    queryset = Company.objects.all()
    serializer_class = CompanyModelSerializer
    # permissions = [IsAdminUser]
