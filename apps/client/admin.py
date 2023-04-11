# From Django
from django.contrib import admin

# My models
from apps.client.models import Client

admin.site.register(Client)