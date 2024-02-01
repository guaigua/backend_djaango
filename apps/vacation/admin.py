# admin.py
from django.contrib import admin
from apps.vacation.models import Vacation, VacationCalendar



admin.site.register(Vacation)
admin.site.register(VacationCalendar)
