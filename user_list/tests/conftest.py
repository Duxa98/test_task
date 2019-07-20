import pytest
from rest_framework.test import APIClient, APIRequestFactory

from user_list import apiviews

from user_list.models import AppUser

# @pytest.fixture
# def django_db_setup():
#     pass

pytestmark = pytest.mark.django_db


@pytest.fixture(params=[1, 2])
def user(db, request):
    for i in range(request.param):
        AppUser.objects.create(
            login=f'login_{i}',
            weight=i * 10
        )
    return request.param


@pytest.fixture
def client(db):
    return APIClient()


@pytest.fixture
def factory():
    return APIRequestFactory()


@pytest.fixture
def list_view(db):
    return apiviews.AppUserViewSet.as_view({'get': 'list'})
