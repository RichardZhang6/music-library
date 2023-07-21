import abc
from typing import List
from datetime import datetime

# from music.domainmodel.track import Track, Review
# from music.domainmodel.user import User
# from music.domainmodel.album import Album
# from music.domainmodel.genre import Genre
# from music.domainmodel.artist import Artist
from music.domainmodel.model import Track, Review, User, Genre, Album, Artist

repo_instance = None

class RepositoryException(Exception):

    def __init__(self, message=None):
        pass

class AbstractRepository(abc.ABC):
    @abc.abstractmethod
    def add_user(self, user: User):
        raise NotImplementedError

    @abc.abstractmethod
    def get_user(self, user_name) -> User:
        raise NotImplementedError

    @abc.abstractmethod
    def add_track(self, track: Track):
        raise NotImplementedError

    def add_album(self, album: Album):
        raise NotImplementedError

    def add_artist(self, artist: Artist):
        raise NotImplementedError

    def add_genre(self, genre: Genre):
        raise NotImplementedError

    #@abc.abstractmethod
    #def get_track(self, id: int) -> Track:
        #raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_by_page(self, num: int) -> List[Track]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_page(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_page(self) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def get_prev_page(self, page_num: int) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def get_next_page(self, page_num: int) -> int:
        raise NotImplementedError

    @abc.abstractmethod
    def add_review_repo(self, review: Review):
        if review.track is None or review not in review.track.reviews:
            raise RepositoryException('Review not correctly attached to a Track')
        if review.user is None or review not in review.user.reviews:
            raise RepositoryException('Review not correctly attached to a User')

    # @abc.abstractmethod
    # def get_reviews(self):
    #     raise NotImplementedError

    @abc.abstractmethod
    def get_track_by_id(self, track_id: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_track_by_artist(self, name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_by_album(self, name: str):
        raise NotImplementedError

    @abc.abstractmethod
    def get_tracks_by_genre(self, type: str):
        raise NotImplementedError

    # @abc.abstractmethod
    # def make_review(self, review_text: str, rating: int, user: User, track: Track, timestamp: datetime = datetime.today()):
    #     raise NotImplementedError
