# django_shop_rest_api# GoCardless sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/AllanMuhari/django_shop_rest_api.git
$ cd SHOP_API
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv venv
$ . myvenv/Scripts/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up.

Once `pip` has finished downloading the dependencies:

```sh
(env) cd project
(env) python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/Admin/`.

## Tests

```sh
(env)$ python manage.py test api.tests
(env)$ python manage.py test api.tests_selenium
```
