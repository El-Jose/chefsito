
def test_my_register(tclient):
    response = tclient.post('/register', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert 'register successful' in response.get_data(as_text=True)


def test_my_login(tclient):
    response = tclient.post('/login', json={'email': 'kazu@gmail.com', 'password': 'toradesu'})
    assert response.status_code == 200
    assert '"correct password"\n' in response.get_data(as_text=True)   
