install:
	pip install -r core/requirements.txt

app:
	gunicorn --chdir core app:app

tests:
	python -m unittest core.tests

