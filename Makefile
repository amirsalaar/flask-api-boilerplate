local-setup:
	pip install --upgrade pip
	pip install poetry
	poetry install
	poetry shell # activates the virtual environment you isntalled with pipenv
	pre-commit install # runs the pre-commit CLI command from within pipenv
	pre-commit autoupdate # runs the pre-commit CLI command from within pipenv
run:
	python app.py
tests:
	pytest
remote-build:
	docker build --target build -t PROJECT-NAME:build .
remote-test:
	docker build --target flask-tests -t PROJECT-NAME:test .
remote-run:
	docker build --target deploy -t PROJECT-NAME:latest .
