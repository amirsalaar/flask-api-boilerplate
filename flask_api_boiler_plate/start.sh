pip install pipenv
SYSTEM_VERSION_COMPAT=1 pipenv sync  # installs the dependencies specified in the Pipfile.lock
pipenv run pre-commit install # runs the pre-commit CLI command from within pipenv
pipenv run  pre-commit autoupdate # runs the pre-commit CLI command from within pipenv
pipenv shell # activates the virtual environment you isntalled with pipenv
export FLASK_APP=manage.py
