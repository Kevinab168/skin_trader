from skin_trader.users.models import User


def test_user_api(db, api_client, user):
    response = api_client.get(f'http://localhost:8000/api/users/{user.id}/')
    assert response.status_code == 200
    data = response.json()
    assert data.get('username') == user.username


def test_create_user(db, api_client):
    username = 'test'
    password = 'test'
    response = api_client.post('http://localhost:8000/api/users/', {
        'username': username,
        'password': password,
    })
    status_code = 201
    assert response.status_code == status_code
    assert User.objects.filter(username=username).exists()


def test_update_user(db, api_client, user_factory):
    user = user_factory.create()
    updated_username = 'Test'
    response = api_client.put(
        f'http://localhost:8000/api/users/{user.id}/',
        {
            'username': updated_username,
            'password': user.password,
        },
        format='json',
    )
    assert response.status_code == 200
    assert User.objects.filter(username=updated_username).exists()


def test_delete_user(db, api_client, user_factory):
    user = user_factory.create()
    response = api_client.delete(f'http://localhost:8000/api/users/{user.id}/')
    assert response.status_code == 204
    assert not User.objects.first()


def test_many_users(db, api_client, user_factory):
    users = user_factory.create_batch(10)
    retrieved_users = User.objects.all()
    assert len(retrieved_users) == len(users)
    response = api_client.get('http://localhost:8000/api/users/')
    users_in_response = response.json()
    assert len(users_in_response) == len(users)
