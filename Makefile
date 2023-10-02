
.PHONY: tests

install:
	pip install -r core/requirements.txt

app:
	gunicorn --chdir core app:app

tests:
	PYTHONPATH=. pytest

