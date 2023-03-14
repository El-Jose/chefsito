
def test_register(test_client):
    response = test_client.post('/register', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert 'register successful' in response.get_data(as_text=True)


def test_login_login(test_client):
    response = test_client.post('/login', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert '"correct password"\n' in response.get_data(as_text=True)   
