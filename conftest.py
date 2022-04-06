from typing import Dict
from urllib.parse import uses_relative
from base import AuthorisedHeader, create_user_api, generate_email, login, delete_profile
import pytest
import random


@pytest.fixture(scope='session', autouse=True)
def user_data() -> Dict:
    body = {'email': generate_email(),
            'employeeId': str(random.randint(100, 100000))
            }

    response = create_user_api(body).json()
    body = {'email': response['email'],
            'password': 'remote236'
            }
    user_data_dict = login(body).json()
    print(user_data_dict)
    yield user_data_dict
    
    e = AuthorisedHeader(user_data_dict)
    header = e.header

    r = delete_profile(header) 





