import pytest

from app import current_app, db
from app.login.models import User


@pytest.fixture(scope='module')
def test_client():
    with current_app.test_client() as client:
        yield client


@pytest.fixture(scope='module')
def init_database(tclient):
    # Create the database and the database table
    db.create_all()

    # Insert user data
    user1 = User(email='userone@gmail.com', password_plaintext='contraseñauwu')
    user2 = User(email='usertwo@gmail.com', password_plaintext='uwucontraseña')
    db.session.add(user1)
    db.session.add(user2)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

