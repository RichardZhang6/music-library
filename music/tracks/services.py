from typing import List, Iterable

from music.adapters.repository import AbstractRepository
# from music.domainmodel.track import Track, Review
from music.domainmodel.model import Track, Review, User, Genre, Album, Artist
from music.domainmodel.make_review import make_review

class NonExistentTrackException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_first_page(repo: AbstractRepository):
    page = repo.get_first_page()
    return page

def get_last_page(repo: AbstractRepository):
    page = repo.get_last_page()
    return page

def get_tracks_by_page(page_num:int, repo: AbstractRepository):
    page = repo.get_tracks_by_page(num = page_num)
    prev_page = repo.get_prev_page(page_num)
    next_page = repo.get_next_page(page_num)
    return page, prev_page, next_page

def get_track_by_id(id: int, repo: AbstractRepository):
    return repo.get_track_by_id(id)

def get_track_by_artist(name: str, repo: AbstractRepository):
    return repo.get_track_by_artist(name)

def get_tracks_by_album(name: str, repo: AbstractRepository):
    return repo.get_tracks_by_album(name)

def get_tracks_by_genre(type: str, repo: AbstractRepository):
    return repo.get_tracks_by_genre(type)
def add_review(track_id: int, review_text: str, rating: int, username: str, repo: AbstractRepository):
    track = repo.get_track_by_id(track_id)
    if track is None:
        raise NonExistentTrackException

    user = repo.get_user(username)
    if user is None:
        raise UnknownUserException

    review = repo.make_review(review_text, rating, user, track)
    repo.add_review_repo(review)

def get_reviews_for_track(track_id, repo: AbstractRepository):
    track = repo.get_track_by_id(track_id)

    if track is None:
        raise NonExistentTrackException

    return track.reviews

def review_to_dict(review: Review):
    review_dict = {
        'user_name': review.user.user_name,
        'track_id': review.track.id,
        'review_text': review.review_text,
        'timestamp': review.timestamp
    }
    return review_dict

def reviews_to_dict(reviews: Iterable[Review]):
    return [review_to_dict(review) for review in reviews]