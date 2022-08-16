# backend_djaango


docker exec -it backend_django_app_1 python manage.py makemigrations
docker exec -it backend_django_app_1 python manage.py migrate 
docker exec -it backend_django_app_1 python manage.py createsuperuser --username admin