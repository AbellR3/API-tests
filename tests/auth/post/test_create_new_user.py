import pytest

import random
from STATIC import auth_url
from base import create_user_api, generate_email






def test_create_new_user():
    id = str(random.randint(100,100000))
    email = generate_email()
    body = {'email':email,
            'employeeId':id
        }

    response = create_user_api(body)
    assert response.status_code == 201

    response_dict = response.json()
    assert str(response_dict['employeeId']) == body['employeeId']
    assert response_dict['email'] == body['email']

@pytest.mark.parametrize('email, employeeId',[
    (generate_email(),'dasdz'),
    (112,'2222'),
    ('asdasda',22),
    ('','')])
def test_create_new_user_negative(email, employeeId):
    body = {'email':email,
        'employeeId':employeeId,
        }
    response = create_user_api(body)
    assert response.status_code == 422 or 500
