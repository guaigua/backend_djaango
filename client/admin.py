# From Django
from django.contrib import admin

# My models
from client.models import Clients

admin.site.register(Clients)