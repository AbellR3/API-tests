import re
from xml.dom.minidom import Element
import pytest
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
    elem = random.choice(response_dict)
    for i in elem:
        assert i in ['id', 'email', 'employeeId', 'isDefaultPassword']

