[![Build Status](https://travis-ci.org/diegosorrilha/work-at-olist.svg?branch=master)](https://travis-ci.org/diegosorrilha/work-at-olist)
[![codecov](https://codecov.io/gh/diegosorrilha/work-at-olist/branch/master/graph/badge.svg)](https://codecov.io/gh/diegosorrilha/work-at-olist)

[The application can be accessed here.
](https://olist-diego.herokuapp.com/)

## Installation
0. Install Python 3.7
1. Install Pipenv
2. Clone this repository
3. Change to the directory was created
4. Install development requirements
5. Configure instance with .env
6. Run tests
7. Run the application

With Python 3.7 installed, run:
```bash
pip install pipenv
git clone git@github.com:diegosorrilha/work-at-olist.git
cd work-at-olist
pipenv sync -d
cp contrib/env-sample .env
pipenv run pytest --cov=phonebills
pipenv run python manage.py runserver
```

## Development
- Run `make dev` to run development server
- Run tests with `make test`
- Run `make pep8` to check the code style

## Deploying
```bash
heroku apps:create myapp
heroku config:set SECRET_KEY=my-secure-secret-key
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS=myapp.herokuapp.com
git push heroku master
```

## Description of the work environment used

### Computer
* MacBook Pro (13-inch, Mid 2012)
* Core i5
* RAM 10GB
* SSH 120GB
* HDD 500GB

### Operating System
* macOS High Sierra (10.13.6)

### Hosting
* Heroku

### Continuous Integration
* Travis CI

### Languages and frameworks
* Python 3.7.0
* Django 2
* Django Rest Framework 3

### Database
* PostgreSQL

### Libraries
* To store config in the environment
    - python-decouple
* To help with database configurations 
    - dj-database-url
* To help with tests:
    - pytest;
    - pytest-django; 
    - pytest-cov;
    - coverage;
    - codecov;
* To help with PEP8: 
    - flake8

### Tools
* IDE:
    - PyCharm 2018.2.2
* To a manual tests and verifications
    - iPython
* Dependency management
    - Pipenv
* Version-control system:
    - Git
    - GitHub
