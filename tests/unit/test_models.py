from app.login.models import User


def test_new_user():
    try_user = User('bateman@gmail.com', 'TWisaN')
    assert try_user.email == 'bateman@gmail.com'
    assert try_user.password != 'TWisaN'
    assert try_user.role == 'user'
