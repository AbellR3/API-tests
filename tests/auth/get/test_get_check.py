import pytest
import requests
from base import AuthorisedHeader
from STATIC import auth_url




def test_check_auth(user_data):
    e = AuthorisedHeader(user_data)
    headers = e.header
    response = requests.request(
    'GET', auth_url+'/api/auth/check', headers=headers)
    assert response.status_code == 200

def test_check_auth(user_data):
    response = requests.request(
    'GET', auth_url+'/api/auth/check', headers={})
    assert response.status_code == 401, ''
    assert response.json()['message'] == 'Невалидный токен','"message": "Невалидный токен"'
    

