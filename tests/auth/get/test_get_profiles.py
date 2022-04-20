
from tests.src.pydandic_shemas.get_prifiles_schema import Profile
import requests
from base import AuthorisedHeader, ResponseValidator
from STATIC import auth_url
import random


def test_get_profiles(user_data):
    e = AuthorisedHeader(user_data)
    headers = e.header
    response = requests.request(
        'GET', auth_url+'/api/auth/profiles', headers=headers)

    response = ResponseValidator(response)

    response.assert_status_code(200).validator(Profile)
