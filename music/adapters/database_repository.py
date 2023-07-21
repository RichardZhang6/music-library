from datetime import date, datetime
from typing import List


from sqlalchemy import desc, asc
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.orm import scoped_session

from music.domainmodel.model import Track, Review, User, Genre, Album, Artist
from music.adapters.repository import AbstractRepository

class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_user(self, user: User):
        with self._session_cm as scm:
            scm.session.add(user)
            scm.commit()

    def get_user(self, user_name: str) -> User:
        user = None
        try:
            user = self._session_cm.session.query(User).filter(User._User__user_name == user_name).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return user

    def add_track(self, track: Track):
        with self._session_cm as scm:
            scm.session.merge(track)
            scm.commit()

    def add_album(self, album: Album):
        with self._session_cm as scm:
            scm.session.merge(album)
            scm.commit()

    def add_artist(self, artist: Artist):
        with self._session_cm as scm:
            scm.session.merge(artist)
            scm.commit()

    def add_genre(self, genre: Genre):
        with self._session_cm as scm:
            #scm.session.add(genre)
            scm.session.merge(genre)
            scm.commit()

    def add_review_repo(self, review: Review):
        super().add_review_repo(review)
        with self._session_cm as scm:
            scm.session.merge(review)
            scm.commit()

    def get_tracks_by_page(self, num: int) -> List[Track]:
        tracks = self._session_cm.session.query(Track).limit(20).offset((num - 1) * 20)
        return tracks

    def get_first_page(self) -> int:
        #tracks = self._session_cm.session.query(Track).limit(20)
        #return tracks
        return 1

    def get_last_page(self) -> int:
        #tracks = self._session_cm.session.query(Track).order(Track.track_id.desc()).limit(20)
        #return tracks
        return self._session_cm.session.query(Track).count() // 20

    def get_next_page(self, page_num: int) -> int:
        #tracks = self._session_cm.session.query(Track).limit(20).offset(page_num * 20)
        return page_num + 1

    def get_prev_page(self, page_num: int) -> int:
        tracks = self._session_cm.session.query(Track).limit(20).offset((page_num - 2) * 20)
        return page_num - 1

    def get_track_by_id(self, track_id: int):
        track = None
        try:
            track = self._session_cm.session.query(Track).filter(Track._Track__track_id == track_id).one()
        except NoResultFound:
            pass
        return track

    def get_tracks_by_album(self, name: str):
        tracks = list()
        row = self._session_cm.session.execute("SELECT album_id FROM albums WHERE title LIKE '%{}%'".format(name)).fetchone()
        if row is None:
            tracks = list()
        else:
            album_id = row[0]
            tracks = self._session_cm.session.execute('SELECT * FROM tracks LEFT JOIN albums on tracks.album_id = albums.album_id WHERE albums.album_id = :id', {'id': album_id})
        return tracks

    def get_track_by_artist(self, name: str):
        tracks = list()
        row = self._session_cm.session.execute("SELECT artist_id FROM artists WHERE full_name LIKE '%{}%'".format(name)).fetchone()
        if row is None:
            tracks = list()
        else:
            artist_id = row[0]
            tracks = self._session_cm.session.execute('SELECT * FROM tracks LEFT JOIN artists on tracks.artist_id = artists.artist_id WHERE artists.artist_id = :id', {'id': artist_id})
        return tracks

    def get_tracks_by_genre(self, type: str):
        tracks = []
        row = self._session_cm.session.execute("SELECT genre_id FROM genres WHERE name LIKE '%{}%'".format(type)).fetchone()
        if row is None:
            tracks = list()
        else:
            genre_id = row[0]
            tracks = self._session_cm.session.execute('SELECT * FROM tracks LEFT JOIN track_genre on tracks.track_id = track_genre.track_id WHERE track_genre.genre_id = :id', {'id': genre_id})
        return tracks

    def make_review(self, review_text: str, rating: int, user: User, track: Track, timestamp: datetime = datetime.today()):
        review = Review(track, review_text, rating)
        user.add_review(review)
        track.add_review(review)
        return review




