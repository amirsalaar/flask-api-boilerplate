import pytest
from pytest_mock.plugin import MockerFixture
from app import create_app


@pytest.fixture(scope="module")
def test_client():
    app = create_app({"TESTING": True})
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
