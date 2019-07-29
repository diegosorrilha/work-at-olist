dev:
	pipenv run python manage.py runserver -v2


test:
	pipenv run pytest --cov=phonebills


pep8:
	pipenv run flake8 .
