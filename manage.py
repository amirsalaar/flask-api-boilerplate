"""Manager script to run the commands on the Flask API."""
import os
import click
from app import create_app

app = create_app()


@app.cli.command("tests")
@click.argument("option", required=False)
def run_test_with_option(option: str = None):
    from subprocess import run
    from shlex import split

    if option is None:
        run(
            [
                "pytest",
                "--disable-pytest-warnings",
                "--cov=lib",
                "--cov-config=.coveragerc",
                "--cov-report=term",
                "--cov-report=xml",
                "--cov-report=html",
                "--junitxml=./tests/coverage/junit.xml",
                "--cov-append",
                "--no-cov-on-fail",
            ]
        )

    elif option == "watch":
        run(
            split(
                'ptw --runner "python3 -m pytest tests --durations=5 '
                '--disable-pytest-warnings"'
            )
        )
    elif option == "debug":
        run(
            split(
                'ptw --pdb --runner "python3 -m pytest tests --durations=5 '
                '--disable-pytest-warnings"'
            )
        )


if __name__ == "__main__":
    HOST = os.getenv("FLASK_RUN_HOST", default="127.0.0.1")
    PORT = os.getenv("FLASK_RUN_PORT", default=5000)
    DEBUG = os.getenv("FLASK_DEBUG", default=False)

    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG,
    )
