import pytest
import requests
from base import AuthorisedHeader
from STATIC import auth_url


def test_sign_out(user_data):
    e = AuthorisedHeader(user_data)
    headers = e.header
    response = requests.request(
    'GET', auth_url+'/api/auth/signout', headers=headers)
    assert response.status_code == 200


def test_sign_out_negative(user_data):

    response = requests.request(
    'GET', auth_url+'/api/auth/signout', headers={})
    assert response.status_code == 400
