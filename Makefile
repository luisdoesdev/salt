
.PHONY: tests
.TEST ?= .

install:
	pip install -r core/requirements.txt

app:
	gunicorn --chdir core app:app

tests:
	PYTHONPATH=. pytest --cov=. #-o log_cli=true -o log_cli_level=DEBUG 

tests-reports:
	PYTHONPATH=. pytest $(TEST)  -o log_cli=true -o log_cli_level=INFO -o log_cli_format='%(asctime)s %(levelname)s %(message)s' -o log_cli_date_format='%Y-%m-%d %H:%M:%S' 