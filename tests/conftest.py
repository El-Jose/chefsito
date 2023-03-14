import pytest

from app import current_app


@pytest.fixture(scope='module')
def tclient():
    with current_app.test_client() as test_client:
        yield test_client
