import pytest
import os
from music.domainmodel.model import Artist, Album, Track, Review, User, Genre
from music.adapters.csvdatareader import TrackCSVReader
from typing import List
from music.adapters.repository import RepositoryException

def test_repository_can_add_a_user(in_memory_repo):
    user = User(5,'dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('dave') is user

def test_repository_can_retrieve_a_user(in_memory_repo):
    user = in_memory_repo.get_user('dave')
    assert user == User(5,'dave', '123456789')

def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None

def test_repository_can_add_track(in_memory_repo):
    track = Track(100001, 'Heat Waves')

    in_memory_repo.add_track(track)

    assert in_memory_repo.get_track(100001) is track

def test_repository_can_retrieve_track(in_memory_repo):
    track = in_memory_repo.get_track(2)


    assert track.title == 'Food'

def test_repository_does_not_retrieve_a_non_existent_track(in_memory_repo):
    track = in_memory_repo.get_track(1000000)
    assert track is None

def test_repository_can_retrieve_track_by_page(in_memory_repo):
    tracklist = in_memory_repo.get_tracks_by_page(1)


    assert len(tracklist) == 20

def test_repository_does_not_retrieve_track_when_there_are_no_trackspage(in_memory_repo):
    tracklist = in_memory_repo.get_tracks_by_page(300)
    assert tracklist is None


