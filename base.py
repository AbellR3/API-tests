from urllib import response
import requests
from STATIC import auth_url
import string
import random
import requests
from tests.src.enums.global_enums import GlobalErrorMessages


def generate_email():
    alf = string.ascii_lowercase
    e_name = ''
    for i in range(6):
        e_name += (random.choice(alf))

    for i in range(2):
        e_name += random.choice([str(x) for x in range(0, 10)])
    e_name += '@email.com'
    return e_name


def create_user_api(body={}):
    header = {'accept': 'application/json',
              'Content-Type': 'application/json'
              }
    response = requests.request(
        'POST', auth_url+'/api/auth/signup', json=body, headers=header)
    return response


def login(body={}):
    header = {'accept': 'application/json',
              'Content-Type': 'application/json'
              }
    response = requests.request(
        'POST', auth_url+'/api/auth/signin', json=body, headers=header)
    return response


class AuthorisedHeader:
    def __init__(self, user_data):
        self.header = {'accept': 'application/json',
                       'Content-Type': 'application/json',
                       'authorization': user_data['token']
                       }


def delete_profile(header):
    r = requests.request('DELETE', auth_url + '/api/auth', headers=header)
    return r


class ResponseValidator:
    def __init__(self, response) -> None:
        self.response = response
        self.response_json =response.json()

    def validator(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                 schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self
    
    def assert_status_code(self,status_code):
        assert self.response.status_code == status_code, GlobalErrorMessages.WRONG_STATUS_CODE
        return self
    

