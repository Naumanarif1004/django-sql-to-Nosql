
#Convert Postgres dataset into a JSON-based format, and store it in Mongo DB 

### Technology Stack

- [Python](https://www.python.org/) 3.7.x
- [Django Framework](https://www.djangoproject.com/) 3.2.x
- [Django Rest Framework](http://www.django-rest-framework.org/) 3.12.x
- [Celery](https://docs.celeryproject.org/) 5.1.2


### Installation Guide

Initial setup commands:

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install setuptools wheel
```

Install requirements:
```shell
$ pip install -r requirements.txt
```
Open .env file in main directory and add mongodb connection:
```shell
MONGO_CREDENTIALS = <your_creds_string>

example => MONGO_CREDENTIALS=mongodb+srv://root:<password>@cluster0.kuzco.mongodb.net/myFirstDatabase?retryWrites=true&w=majority

```


Run the development server and Celery worker:

```shell
$ python3 manage.py runserver
$ celery -A test_project worker -l INFO

```