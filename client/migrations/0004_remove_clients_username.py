# Generated by Django 4.0.2 on 2022-03-09 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_clients_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='username',
        ),
    ]
