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


class AuthorisedHeader:
    def __init__(self, user_data):
        self.header = {'accept': 'application/json',
              'Content-Type': 'application/json',
              'authorization': user_data['token']
              }


def delete_profile(header):
    r = requests.request('DELETE', auth_url + '/api/auth', headers=header)
    return r


    
# class Standart_request:
#     def __init__(self, url:str, method:str):
#         self.url = url
#         self.method = method

#     def request(self, body={}):
#         header = {'accept': 'application/json',
#                   'Content-Type': 'application/json'
#                   }
#         response = requests.request(
#             self.method, auth_url+'/api/auth/signin', json=body, headers=header)
#         return response


