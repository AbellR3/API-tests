from urllib import request

import pytest
from base import AuthorisedHeader, generate_email, auth_url
import requests


@pytest.mark.skip(reason='Not correct api')
def test_update_email(user_data):
    e = AuthorisedHeader(user_data)
    header = e.header
    print(header)
    old_email = user_data['email']
    new_email = generate_email()
    body = {'oldEmail':old_email,
            'newEmail':new_email,
    }
    response = requests.request('PATCH', url= auth_url + '/api/auth/email', json=body, headers= header)
    print(response.status_code, response.text)
    assert response.status_code == 200
    response_dict = response.json()
  
    assert response_dict['email'] == new_email
