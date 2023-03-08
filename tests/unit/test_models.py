
from app.login.models import User


from app import create_app
from flask import url_for

def test_new_user():
    try_user = User('bateman@gmail.com', 'TWisaN')
    assert try_user.email == 'bateman@gmail.com'
    assert try_user.password == 'TWisaN'

def test_new_user_2():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password_hashed, authenticated, and active fields are defined correctly
    """
    user = User('bateman@gmail.com', 'TWisaN')
    assert user.email == 'bateman@gmail.com'
    assert user.password != 'TWisaN'
    assert user.__repr__() == '<User: bateman@gmail.com>'
    assert user.is_authenticated
    assert user.is_active
    assert not user.is_anonymous
