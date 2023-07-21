from datetime import date, datetime

import pytest

import music.adapters.repository as repo
from music.adapters.database_repository import SqlAlchemyRepository
from music.domainmodel.model import User, Artist, Review, Track, Genre, Album
from music.adapters.repository import RepositoryException

def test_repository_can_add_a_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    user = User('Dave', '123456789')
    repo.add_user(user)

    repo.add_user(User('Martin', '123456789'))

    # user2 = repo.get_user('Dave')

    assert user is user

def test_repository_does_not_retrieve_a_non_existent_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    user = repo.get_user('prince')
    assert user is None

def test_repository_can_retrieve_track_count(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    number_of_tracks = repo.get_track_by_id(1)



    assert number_of_tracks is number_of_tracks

# def test_repository_can_add_article(session_factory):
#     repo = SqlAlchemyRepository(session_factory)
#
#     number_of_articles = repo.get_number_of_articles()
#
#     new_article_id = number_of_articles + 1
#
#     track = Article(
#         date.fromisoformat('2020-03-09'),
#         'Second US coronavirus cruise tests negative amid delays and cancellations',
#         'It was revealed ...',
#         'https://www.nzherald.co.nz/travel/news/article.cfm?c_id=7&objectid=12315024',
#         'https://www.nzherald.co.nz/resizer/ix7hy3lzkMWUkD8hE6kdZ-8oaOM=/620x349/smart/filters:quality(70)/arc-anglerfish-syd-prod-nzme.s3.amazonaws.com/public/7VFOBLCBCNDHLICBY3CTPFR2L4.jpg',
#         new_article_id
#     )
#     repo.add_track(article)
#
#     assert repo.get_article(new_article_id) == article
#
def test_repository_can_retrieve_track(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    track = repo.get_track_by_id(2)

    # Check that the Article has the expected title.
    assert track.title == 'Food'

def test_repository_does_not_retrieve_a_non_existent_track(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    track = repo.get_track_by_id(9999)
    assert track is None

def test_repository_retrieve_a_track_by_page(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    track = repo.get_tracks_by_page(3)
    assert track is track

def test_does_not_retrieve_a_nonexistent_page(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    track = repo.get_tracks_by_page(400)
    assert track is track

def test_can_get_first_page(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    track = repo.get_first_page()
    assert track ==1

def test_can_get_last_page(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    track = repo.get_last_page()
    assert track == 100

def test_can_get_previous_page(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    prevpage = repo.get_prev_page(10)
    assert prevpage == 9

def test_can_get_next_page(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    nextpage = repo.get_next_page(10)
    assert nextpage == 11

def test_return_first_page_when_there_are_no_prev_page(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    prevpage = repo.get_prev_page(1)
    assert prevpage is prevpage

def test_return_last_page_when_there_are_no_next_page(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    nextpage = repo.get_next_page(100)
    assert nextpage is nextpage

def test_repository_does_not_add_a_review_without_a_user(session_factory):
    repo = SqlAlchemyRepository(session_factory)

    track = repo.get_track_by_id(2)
    review = Review(track, "BLAH!", 1)

    with pytest.raises(RepositoryException):
        repo.add_review_repo(review)

