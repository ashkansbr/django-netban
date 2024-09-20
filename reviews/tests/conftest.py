import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user(db):
    def make_user(email="testuser@example.com", password="password123"):
        user = User.objects.create_user(email=email, password=password)
        return user
    return make_user

@pytest.fixture
def authenticate_user(api_client, create_user):
    user = create_user()
    response = api_client.post('/api/token/', {'email': user.email, 'password': 'password123'}, format='json')
    token = response.data['access']
    api_client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return user
