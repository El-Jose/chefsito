
from app.login.models import User


def test_new_user():
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email, password
    """
    try_user = User('bateman@gmail.com', 'TWisaN')
    assert try_user.email == 'bateman@gmail.com'
    assert try_user.password == 'TWisaN'
