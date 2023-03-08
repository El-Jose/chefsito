
def test_login(test_client):
    response = client.post('/login', data={'email': 'usuario@ejemplo.com', 'password': 'contraseña'})
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Inicio de sesión exitoso!'

def test_login_invalid_credentials(test_client):
    response = client.post('/login', data={'email':'monda@gmail.com', 'password':'contraseña_incorrecta'})
    assert response.status_code == 200
    assert response.get_data(as_text=True) == 'Credenciales incorrectas!'


def test_login_page(test_client):

    response = test_client.get('/login')
    assert response.status_code == 200
    assert b'Email' in response.json
    assert b'Password' in response.json
