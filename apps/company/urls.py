# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from apps.company import views

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


schema_view = get_schema_view(
    openapi.Info(
        title="Company",
        default_version='v1',
        description="Includes all resource methods",
        contact=openapi.Contact(email="admin@uni.cloud"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

router = DefaultRouter()
router.register(r'company', views.CompanyViewSet, basename='accounts')

urlpatterns = [
    path('', include(router.urls))
]