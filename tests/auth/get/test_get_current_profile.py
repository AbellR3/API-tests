from base import auth_url, AuthorisedHeader
import requests


def test_get_current_prifile(user_data):
    '''This test assert that profile have correct token'''
    e = AuthorisedHeader(user_data)
    header = e.header
    response = requests.request('GET', auth_url + '/api/auth/current-profile', headers=header)
    assert response.status_code == 200
    response_dict = response.json()
    assert response_dict['token'] == user_data['token'], 'Not correct token'
    assert response_dict['id'] == user_data['id']

def test_get_current_prifile_negative(user_data):
    e = AuthorisedHeader(user_data)
    header = e.header
    header['authorization'] = 'asdxcbv234ased1da2ease1'
    response = requests.request('GET', auth_url + '/api/auth/current-profile', headers=header)
    assert response.status_code == 401
    response_dict = response.json()
