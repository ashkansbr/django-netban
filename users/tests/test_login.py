import pytest


@pytest.mark.django_db
def test_user_can_login(api_client, create_user):
    user = create_user()
    response = api_client.post('/api/login/', {'username': user.username, 'password': 'password123'}, format='json')

    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data
