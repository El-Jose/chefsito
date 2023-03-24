import pytest

from app import current_app, db
from app.login.models import User


@pytest.fixture(scope='module')
def test_client():
    with current_app.test_client() as client:
        yield client


@pytest.fixture(scope='module')
def init_database(test_client):
    db.create_all()


    user1 = User(email='userone@gmail.com', password='correct')
    user2 = User(email='usertwo@gmail.com', password='uwucontraseña')
    user3 = User(email='userthree@gmail.com', password='passworduwu')
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)
    db.session.commit()

    usertest = User.query.filter_by(email='userthree@gmail.com').first()
    usertest.temp_num = 111114
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()

