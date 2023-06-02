#!/usr/bin/env python
from apps.accounts.models import User

#Create User Admin

user=User.objects.create_user('admin', password='@@admin1234')
user.is_superuser=True
user.is_staff=True
user.email='admin@admin.com'
user.save()
