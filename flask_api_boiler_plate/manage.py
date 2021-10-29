import os
import pytest
import click
from dotenv import load_dotenv
from app import create_app

load_dotenv()
app = create_app()


@app.cli.command("tests")
@click.argument("option", required=False)
def run_test_with_option(option: str = None):
    from subprocess import run
    from shlex import split

    if option is None:
        pytest.main(
            [
                "--disable-pytest-warnings",
                "--cov=.",
                "--cov-report=xml",
                "--cov-config=.coveragerc",
                "--cov-append",
            ]
        )
    elif option == "coverage":
        pytest.main(
            [
                "--disable-pytest-warnings",
                "--cov=.",
                "--cov-report=html",
                "--cov-config=.coveragerc",
                "--cov-append",
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
    app.run(
        host=os.getenv("FLASK_RUN_HOST"),
        port=os.getenv("FLASK_RUN_PORT"),
        debug=os.getenv("FLASK_DEBUG"),
    )
