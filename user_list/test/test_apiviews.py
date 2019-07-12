import pytest
from django.test import Client
# from django.urls import reverse

from rest_framework.reverse import reverse

from user_list.models import AppUser


@pytest.fixture(scope='function', params=[1, 2])
def django_client_setup(db, request):

    for i in range(request.param):
        AppUser(login=f'login_{i}', weight=i * 10).save()

    return request.param


def test_apiviews(django_client_setup):
    c = Client()
    resp = c.get(reverse('list'))
    assert resp.status_code == 200
    ans = resp.json()

    print(ans)

    param = django_client_setup

    assert len(ans) == param

    for i in range(param):
        assert ans[i]['login'] == f'login_{i}'
        assert ans[i]['weight'] == i * 10

