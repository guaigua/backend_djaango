"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

# Code made to generate Swagger documentation automatically through drf_yasg
schema_view = get_schema_view(
    openapi.Info(
        title="Backend APIs",
        default_version='v1',
        description="APIs Broker",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
router = routers.DefaultRouter()
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    #accounts
    path('', include(('apps.accounts.urls', 'accounts'), namespace='accounts')),
    # client
    path('', include(('apps.client.urls', 'client'), namespace='client')),

    # company
    path('', include(('apps.company.urls', 'company'), namespace='company')),

    # vacation
    path('', include(('apps.vacation.urls', 'vacation'), namespace='vacation')),

    #swagger
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json'
    ),
    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui'
    ),
    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'
    )
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
