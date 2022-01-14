local-setup:
	pip install pipenv
	SYSTEM_VERSION_COMPAT=1 \
		PIPENV_IGNORE_VIRTUALENVS=1 \
		PIPENV_VENV_IN_PROJECT=true \
		pipenv install --dev --pre # installs the dependencies specified in the Pipfile
	pipenv run pre-commit install # runs the pre-commit CLI command from within pipenv
	pipenv run  pre-commit autoupdate # runs the pre-commit CLI command from within pipenv
	pipenv shell # activates the virtual environment you isntalled with pipenv
	export FLASK_APP=manage.py
run:
	flask run
tests:
	export FLASK_APP=manage.py
	flask tests
remote-build:
	docker build --target build -t PROJECT-NAME:build .
remote-test:
	docker build --target flask-tests -t PROJECT-NAME:test .
remote-run:
	docker build --target deploy -t PROJECT-NAME:latest .
