# import pytest
# from django.test import Client
# from django.urls import reverse

# from rest_framework.reverse import reverse
import pytest


# TODO: DRY(creating every time)

def test_list_view(factory, list_view):
    path = '/users/'
    request = factory.get(path)
    response = list_view(request)

    assert response.status_code == 200


def test_list_data(user, client, factory):
    path = '/users/'
    response = client.get(path)

    assert response.status_code == 200

    ans = response.json()
    param = user

    assert len(ans) == param

    for i in range(param):
        assert ans[i]['login'] == f'login_{i}'
        assert ans[i]['token'] == f'login_{i}_token'
        assert float(ans[i]['weight']) == float(i * 10)


def test_info_view(factory, list_view):  # TODO: how to test view separately
    path = '/users/'
    request = factory.get(path)
    response = list_view(request)

    assert response.status_code == 200


def test_info_data(user, client):
    base_path = '/users/'
    param = user

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


# def test_create_fail(client):  # TODO: think its not my business
#     path = '/users/'
#     login = 'any_login'
#     data = {
#         'login': login
#     }
#     response = client.post(path, data=data, format='json')
#
#     assert response.status_code == 201
#
#     response = client.post(path, data=data, format='json')
#
#     assert response.status_code == 400
#
#     response = client.post(path, data={}, format='json')
#
#     assert response.status_code == 400

def test_update_view():
    pass


def test_update(user, client):
    param = user
    path = '/users/'
    for i in param:
        data = {
            'login': f'login_{i}',
            'weight': i * 100
        }
        response = client.put(path, data=data, format='json')

        # assert response.status_code ==


def test_delete():
    pass
