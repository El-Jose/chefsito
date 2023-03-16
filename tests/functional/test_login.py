

REGISTER_VIEW_MSG ={
    "succesfull": "register successful",
    "correct": "correct password",
    "Login ERROR": "error trying to login",
    "Register ERROR": 'error to register',
}


def test_register(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/register', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert REGISTER_VIEW_MSG['succesfull'] in response.json  #RESPONSE.JSON CAMBIO


def test_login_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert REGISTER_VIEW_MSG['correct'] in response.json 


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
    assert REGISTER_VIEW_MSG["Login ERROR"] in response.get_data(as_text=True)


def test_valid_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid and the user is logged in
    """
    response = test_client.post('/register',
        json={'email': 'user1@gmail.com',
        "password": 'passunu'},
        follow_redirects=True)
    assert response.status_code == 200
    assert REGISTER_VIEW_MSG['succesfull'] in response.json


def test_duplicate_registration(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST) using an email address already registered
    THEN check an error message is returned to the user
    """
    # Try registering with the same email address
    response = test_client.post('/register',
        json={"email": 'userone@gmail.com',
        "password": 'contraseñauwu'},follow_redirects=True)
    assert response.status_code == 409
    assert REGISTER_VIEW_MSG["Register ERROR"] in response.get_data(as_text=True)
