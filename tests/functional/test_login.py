
def test_register(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/register', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert 'register successful' in response.get_data(as_text=True)


def test_login_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert '"correct password"\n' in response.get_data(as_text=True)   


def test_invalid_login(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to with invalid credentials (POST)
    THEN check an error message is returned to the user
    """
    response = test_client.post('/login',
                                json={'email': 'userone@gmail.com',
                                "password": 'contraseñaunu'},
                                follow_redirects=True)
    assert response.status_code == 501
    assert b"error trying to login" in response.data
