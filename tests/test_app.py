from http import HTTPStatus

# def test_root_deve_retornar_ok_e_ola_mundo():
#     client = TestClient(app)

#     response = client.get('/')

#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'message': 'Olá Mundo!'}


# def test_exercicio_ola_mundo_em_html():
#     client = TestClient(app)

#     response = client.get('/exercicio_html')

#     assert response.status_code == HTTPStatus.OK
#     assert '<p>Olá Mundo</p>' in response.text


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'jamily',
            'email': 'jamily@gmail.com',
            'password': '1234567',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'jamily',
        'email': 'jamily@gmail.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'jamily',
                'email': 'jamily@gmail.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'jamily_updated',
            'email': 'jamily_updated@gmail.com',
            'password': '1234567',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'jamily_updated',
        'email': 'jamily_updated@gmail.com',
    }


def test_delete_user(client):
    response = client.delete('/users/1/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}

    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'users': []}
