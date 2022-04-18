
from tests.src.pydandic_shemas.get_prifiles_schema import Profile
import requests
from base import AuthorisedHeader
from STATIC import auth_url
import random


def test_get_profiles(user_data):
    e = AuthorisedHeader(user_data)
    headers = e.header
    response = requests.request(
        'GET', auth_url+'/api/auth/profiles', headers=headers)
    assert response.status_code == 200
    response_dict = response.json()
    for item in response_dict:
        Profile.parse_obj(item)
    
    # elem = random.choice(response_dict)
    # for i in elem:
    #     assert i in ['id', 'email', 'employeeId', 'isDefaultPassword']
