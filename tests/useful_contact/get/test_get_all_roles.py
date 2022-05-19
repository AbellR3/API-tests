import requests
from base import AuthorisedHeader, ResponseValidator
from STATIC import auth_url
from tests.src.pydandic_shemas.get_all_roles import AllRoles


def test_get_all_roles(user_data):
    e = AuthorisedHeader(user_data)
    header = e.header
    response = requests.request('GET', url = auth_url + '/roles', headers=header)
    response = ResponseValidator(response)
    response.assert_status_code(200).validator(AllRoles)
   