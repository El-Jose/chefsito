


REGISTER_VIEW_MSG ={
    "register_200": "register successful",
    "register_400": "error to register"}
LOGIN_VIEW_MSG ={
    "login_400": "error trying to login",
    "login_200": "correct password"}


def test_register(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/register', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert REGISTER_VIEW_MSG["register_200"] in response.json  #RESPONSE.JSON CAMBIO


def test_login_login(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert LOGIN_VIEW_MSG["login_200"] in response.json 


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
    assert LOGIN_VIEW_MSG["login_400"] in response.get_data(as_text=True)


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
    assert REGISTER_VIEW_MSG["register_200"] in response.json


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
    assert REGISTER_VIEW_MSG["register_400"] in response.get_data(as_text=True)


RECOVERY_VIEW_MSG = {
    "recovery_400": "Correo electronico no encontrado",
    "recovery_code": 'codigo'}

RESET_VIEW_MSG = {
    "reset_409": 'Las contraseñas no coinciden',
    "reset_400": "El correo electrónico o el código son incorrectos",
    "reset_200": "La contraseña se ha actualizado correctamente"}


def test_recovery_code(test_client):
    """
    GIVEN a Flask aplication configured for testing
    WHEN the '/reset' page is posted to (POST) using an email address 
    THEN check an response message is returned 
    """
    response = test_client.post('/recovery',
        json={"email": 'userone@gmail.com'},follow_redirects=True)
    assert response.status_code == 200
    assert RECOVERY_VIEW_MSG["recovery_code"] in response.json


def test_recovery_email_error(test_client):
    """
    GIVEN a Flask aplication configured for testing
    WHEN the '/recovery' page is posted to (POST) using an email address no created 
    THEN check an error  message is returned 
    """
    response = test_client.post('/recovery',
        json={"email": 'user@gmail.com'},follow_redirects=True)
    assert response.status_code == 400
    assert RECOVERY_VIEW_MSG["recovery_400"] in response.json


def test_password_reset(test_client, init_database):
    """
    GIVEN a Flask aplication configured for testing
    WHEN the '/reset' page is posted to (POST) using an email address, verification code, password, confirm password created
    THEN check the response messege is returned
    """
    response = test_client.post('/reset',
        json={"email":"userthree@gmail.com",
        "codigo":"111114",
        "password":"ellol","confirm":"ellol"})
    assert response.status_code == 200
    assert RESET_VIEW_MSG["reset_200"] in response.json


def test_password_reset_error(test_client):
    """
    GIVEN a Flask aplication configured for testing
    WHEN the '/reset' page is posted to (POST) using an email address, verification code, password, confirm password created
    THEN check the response messege return is an error
    """
    response = test_client.post('/reset',
        json={"email":"userthree@gmail.com",
        "codigo":"111113",
        "password":"ellol","confirm":"ellol"},follow_redirects=True)
    assert response.status_code == 400
    assert RESET_VIEW_MSG["reset_400"] in response.json
