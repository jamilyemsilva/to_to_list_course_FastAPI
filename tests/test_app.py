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
