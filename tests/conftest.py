import pytest

from app.login.models import User, db
from app import create_app

@pytest.fixture(scope='module')
def test_client():
    app = create_app
    with app.test_client() as client:
        yield client