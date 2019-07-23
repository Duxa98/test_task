import pytest

from django.contrib.auth.models import User

from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.authtoken.models import Token

from user_list import apiviews
from user_list.models import AppUser


@pytest.fixture(autouse=True)
def create_admin_user(db):
    user = User(
        email='email@amail.com',
        username='admin'
    )
    user.set_password('admin')
    user.save()
    Token.objects.create(user=user)

@pytest.fixture
def token(db):
    return Token.objects.get(user__username='admin')


@pytest.fixture(params=[1, 2])
def app_user(db, request):
    for i in range(request.param):
        AppUser.objects.create(
            login=f'login_{i}',
            weight=i * 10
        )
    return request.param


@pytest.fixture
def client(db, token):
    # token = Token.objects.get(user__username='admin')
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')
    return client


@pytest.fixture
def factory():
    return APIRequestFactory()


@pytest.fixture
def list_view(db):
    return apiviews.AppUserViewSet.as_view({'get': 'list'})
