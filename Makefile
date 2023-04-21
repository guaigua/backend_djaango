migrate-run:
	chmod +x cli/python
	./cli/python manage.py migrate

migrate-generate:
	chmod +x cli/python
	./cli/python manage.py makemigrations