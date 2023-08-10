The backend of base source code
===================================

To run locally, you can either:

- Install and run from a virtual environment
- Run with docker compose (see below)

Install and run locally from a virtual environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Create a `Python 3.8+ virtualenv and activate it <https://docs.python.org/3/library/venv.html>`_

## 1. Build and run the container

1. Install Docker.

2. Download this repository.

3. Create a `.env` file at the same level as this README, take the example in .env.example. This will be used by Docker.


4. On the command line, within this directory, do this to build the image and
   start the container:

        docker-compose up --build

7. If that's successful you can then start it up. This will start up the database and web server, and display the Django `runserver` logs:

        docker-compose up -d

8. Do you need create user manual (Example):

    docker exec -it django_base python manage.py createsuperuser --username=root@dev.com --email=root@dev.com 


9. Open http://0.0.0.0:8000 in your browser.

10. It's Workingggg

