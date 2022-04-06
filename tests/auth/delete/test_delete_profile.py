import pytest


from base import delete_profile, AuthorisedHeader



@pytest.mark.skip(reason='Not finished api')
def test_delete_profile(user_data):
    e = AuthorisedHeader(user_data)
    header = e.header
    response = delete_profile(header)
    assert response.status_code == 200
    
def test_delete_profile_negative(user_data):
    
    response = delete_profile({})
    assert response.status_code == 404
    