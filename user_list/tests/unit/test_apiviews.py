# import pytest
# from django.test import Client
# from django.urls import reverse

# from rest_framework.reverse import reverse
import pytest


# TODO: DRY(creating every time)

# @pytest.mark.skip
def test_list_view(factory, token, list_view):
    path = '/users/'
    request = factory.get(path, HTTP_AUTHORIZATION=f'Token {token.key}')
    response = list_view(request)
    assert response.status_code == 200


def test_list_data(app_user, client, factory):
    path = '/users/'
    response = client.get(path)

    assert response.status_code == 200

    ans = response.json()
    param = app_user

    assert len(ans) == param

    for i in range(param):
        assert ans[i]['login'] == f'login_{i}'
        assert ans[i]['token'] == f'login_{i}_token'
        assert float(ans[i]['weight']) == float(i * 10)


# @pytest.mark.skip
def test_info_view(factory, token, list_view):  # TODO: how to test view separately
    path = '/users/'
    request = factory.get(path, HTTP_AUTHORIZATION=f'Token {token.key}')
    response = list_view(request)

    assert response.status_code == 200


def test_info_data(app_user, client):
    base_path = '/users/'
    param = app_user

    for i in range(param):
        path = base_path + f'login_{i}/'
        response = client.get(path)

        assert response.status_code == 200

        ans = response.json()

        assert ans['login'] == f'login_{i}'
        assert float(ans['weight']) == float(i * 10)

        assert 'token' not in ans


@pytest.mark.parametrize('login', ['login0', 'логин0'])
def test_create_ok(client, login):
    path = '/users/'
    data = {
        'login': login
    }
    response = client.post(path, data=data, format='json')

    assert response.status_code == 201

    ans = response.json()

    assert ans['login'] == login


# @pytest.mark.skip
def test_update_view():
    pass


def test_update(app_user, client):
    param = app_user
    base_path = '/users/'

    for i in range(param):
        login = f'login_{i}'
        path = base_path + login + '/'
        data = {
            'login': login,
            'weight': i * 100
        }
        response = client.put(path, data=data, format='json')

        assert response.status_code == 200

        ans = response.json()

        assert float(ans['weight']) == float(i * 100)


def test_partial_update(app_user, client):
    param = app_user
    base_path = '/users/'

    for i in range(param):
        login = f'login_{i}'
        path = base_path + login + '/'
        data = {
            'weight': i * 200
        }
        response = client.patch(path, data=data, format='json')

        assert response.status_code == 200

        ans = response.json()

        assert float(ans['weight']) == float(i * 200)


def test_delete(app_user, client):
    path = '/users/login_0/'

    response = client.delete(path)

    assert response.status_code == 204
