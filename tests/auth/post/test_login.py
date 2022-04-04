import pytest
from base import login


def test_login_positive(user_data):
    body = {'email': user_data['email'],
            'password': 'remote236'
            }
    response = login(body)
    assert response.status_code == 201


def test_login_not_correct_date():
    body = {'email': 'simple@email.qqqq',
            'password': 'remote236'
            }
    response = login(body)
    assert response.status_code == 401
    assert response.json()['message'] == "Не верный пароль или email"
