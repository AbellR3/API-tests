import requests
from base import AuthorisedHeader, ResponseValidator
from STATIC import auth_url
from tests.src.enums.global_enums import GlobalErrorMessages



def test_check_auth(user_data):
    e = AuthorisedHeader(user_data)
    headers = e.header
    response = requests.request(
    'GET', auth_url+'/api/auth/check', headers=headers)
    # assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
    ResponseValidator(response).assert_status_code(200)


def test_check_auth(user_data):
    response = requests.request(
    'GET', auth_url+'/api/auth/check', headers={})
    assert response.status_code == 401, GlobalErrorMessages.WRONG_STATUS_CODE.value
    assert response.json()['message'] == 'Невалидный токен','"message": "Невалидный токен"'
    

