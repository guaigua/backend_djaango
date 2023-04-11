from django.contrib import admin

# Register your models here.
# My models
from apps.company.models import Company

admin.site.register(Company)