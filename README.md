# Grunge Rock Development Application

## Overview

This Django project implements a catalogue of Grunge rock music.  It has a fully-functional Django admin interface, and a read-only REST API.  It contains three related data models:

1. `Artist`
2. `Album`
3. `Track`

## Goals

* Implement the ability to fetch, create, update, and delete playlists through the REST API.  A playlist should have a `uuid`, a `name`, and contain 0 or more tracks from this catalogue.  The tracks should be orderable in the playlist.
* Implement the test cases in `tests/test_playlists.py`.  The goal is to have no skipped or failing tests.

## Getting started

### Set up a virtualenv

```shell
$ python3 -m venv venv
$ source venv/bin/activate
```

### Install dependencies

```shell
$ pip install --upgrade pip
$ pip install --requirement=requirements.txt
```

### Initialize the development database

```shell
$ python manage.py migrate
$ python manage.py loaddata initial_data
```

### Add a development superuser

```shell
$ python manage.py createsuperuser
```

### Run the development server

```shell
$ python manage.py runserver
```

Log into the Django admin with your superuser account at:

[http://localhost:8000/admin/](http://localhost:8000/admin/)

Browse the REST API at:

[http://localhost:8000/api/v1/](http://localhost:8000/api/v1/).

## Developing

You can check your work at any time by running:

```shell
$ make ready
```

This will run the default code linters and the test suite.  You can format your code to what the linters expect with:

```shell
$ make format
```