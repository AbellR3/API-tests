from typing import Dict
from base import create_user_api, generate_email, login
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
    user_data_dict = login(body)

    return user_data_dict.json()
