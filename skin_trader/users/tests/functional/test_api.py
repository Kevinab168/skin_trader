def test_user_api(db, api_client, user):
    response = api_client.get('http://localhost:8000/api/users/')
    data = response.json()
    assert response.status_code == 200
    username = data[0].get('username')
    email = data[0].get('email')
    assert username == user.username
    assert email == user.email
