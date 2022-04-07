import requests
from base import AuthorisedHeader, auth_url

def test_get_user_permissions(user_data):
    e = AuthorisedHeader(user_data)
    header = e.header
    response = requests.request('GET', url = auth_url + '/api/auth/permissions', headers=header)
    assert response.status_code == 200
    assert 'permissions' in response.json()[0]
    
def test_get_user_permissions_negative(user_data):
    e = AuthorisedHeader(user_data)
    header = e.header
    response = requests.request('GET', url = auth_url + '/api/auth/permissions', headers=header)
    assert response.status_code == 200
    assert 'permissions' in response.json()[0]
    