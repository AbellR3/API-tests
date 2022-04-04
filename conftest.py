from base import create_user_api, generate_email
import pytest
import random





@pytest.fixture(scope='session')
def create_user():

    body = {'email':generate_email(),
            'employeeId':str(random.randint(100,100000))
        }

    response = create_user_api(body)
    response_dict= response.json()
    
    id = response_dict['id']
    employeeId = response_dict['employeeId']
    email = response_dict['email']
    password = 'remote236'
    return id, employeeId, email, password
