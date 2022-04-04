from email import header
import requests
from STATIC import auth_url
import string
import random


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


class AuthorisedFunc:
    def __init__(self, user_data):
        self.token = user_data['token']

    header = {'accept': 'application/json',
              'Content-Type': 'application/json',
              
              }
