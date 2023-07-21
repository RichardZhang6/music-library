import pytest
from music.authentication.services import AuthenticationException
from music.tracks import services as services
from music.authentication import services as auth_services
from music.tracks.services import NonExistentTrackException

def test_can_add_user(in_memory_repo):
    new_user_name = 'jz'
    new_password = 'abcd1A23'

    auth_services.add_user(new_user_name, new_password, in_memory_repo)

    user_as_dict = auth_services.get_user(new_user_name, in_memory_repo)
    assert user_as_dict['user_name'] == new_user_name


    assert user_as_dict['password'].startswith('pbkdf2:sha256:')


def test_authentication_with_valid_credentials(in_memory_repo):
    new_user_name = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_user_name, new_password, in_memory_repo)

    try:
        auth_services.authenticate_user(new_user_name, new_password, in_memory_repo)
    except AuthenticationException:
        assert False

def test_authentication_with_invalid_credentials(in_memory_repo):
    new_user_name = 'pmccartney'
    new_password = 'abcd1A23'

    auth_services.add_user(new_user_name, new_password, in_memory_repo)

    with pytest.raises(auth_services.AuthenticationException):
        auth_services.authenticate_user(new_user_name, '0987654321', in_memory_repo)

def test_can_get_track(in_memory_repo):
    trackpage = 2

    tracks = services.get_tracks_by_page(trackpage, in_memory_repo)
    assert len(tracks) == 20

def test_cannot_get_track_with_non_existent_page(in_memory_repo):
    trackpage = 1000


    with pytest.raises(services.NonExistentTrackException):
        services.get_tracks_by_page(trackpage, in_memory_repo)

def test_get_first_page(in_memory_repo):
    firstpage = services.get_first_page(in_memory_repo)

    assert firstpage == 1

def test_get_last_page(in_memory_repo):
    lastpage = services.get_last_page(in_memory_repo)

    assert lastpage == 100

def test_get_tracks_by_page_with_non_existent_page(in_memory_repo):
    targetpage = services.get_tracks_by_page(1000)



    assert len(targetpage) == 0


