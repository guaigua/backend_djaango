# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from apps.client import views

router = DefaultRouter()
router.register(r'client', views.ClientViewSet, basename='client')

urlpatterns = [
    path('', include(router.urls))
]