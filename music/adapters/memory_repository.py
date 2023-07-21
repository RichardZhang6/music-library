import csv
from datetime import date, datetime
from typing import List
from pathlib import Path

from music.adapters.repository import AbstractRepository
# from music.domainmodel.track import Track, Review
# from music.domainmodel.user import User
# from music.domainmodel.genre import Genre
from music.domainmodel.model import Track, Review, User, Genre
from music.adapters.csvdatareader import TrackCSVReader

class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__users = list()
        self.__tracks = list()
        self.__reviews = list()

    def add_user(self, user: User):
        self.__users.append(user)

    def get_user(self, user_name) -> User:
        return next((user for user in self.__users if user.user_name == user_name), None)

    def add_track(self, track: Track):
        self.__tracks.append(track)

    def get_track_by_id(self, id: int) -> Track:
        track = None
        for t in self.__tracks:
            if t.track_id == id:
                track = t
        return track


    def get_first_page(self):
        return 1;

    def get_last_page(self):
        return len(self.__tracks) // 20


    def get_tracks_by_page(self, num: int):
        a_list = list()
        for i in range(0, len(self.__tracks), 20):
            if len(self.__tracks) - i >= 20:
                page = self.__tracks[i: i + 20]
            else:
                page = self.__tracks[i: len(self.__tracks)]
            a_list.append(page)
        try:
            if num > 0:
                return a_list[num - 1]
        except:
            pass


    def get_prev_page(self, page_num: int) -> int:
        return page_num - 1

    def get_next_page(self, page_num: int) -> int:
        if page_num < len(self.__tracks) // 20:
            return page_num + 1
        else:
            return len(self.__tracks) // 20

    def add_review_repo(self, review: Review):
        super().add_review_repo(review)
        self.__reviews.append(review)

    def get_reviews(self):
        return self.__reviews

    def get_track_by_artist(self, name: str):
        a_list = []
        for track in self.__tracks:
            if name.lower() in track.artist.full_name.lower():
                a_list.append(track)
        return a_list

    def get_tracks_by_album(self, name: str):
        a_list = []
        for track in self.__tracks:
            album = track.album
            if album is not None and name.lower() in album.title.lower():
                a_list.append(track)
        return a_list

    def get_tracks_by_genre(self, type: str):
        a_list = []
        for track in self.__tracks:
            genres = track.genres
            for genre in genres:
                if type.lower() in genre.name.lower():
                    a_list.append(track)

        return a_list

    def make_review(self, review_text: str, rating: int, user: User, track: Track, timestamp: datetime = datetime.today()):
        review = Review(track, review_text, rating)
        user.add_review(review)
        track.add_review(review)
        return review



def load_tracks(data_path: Path, repo: MemoryRepository, database_mode: bool):
    album_filename = str(data_path / "raw_albums_excerpt.csv")
    track_filename = str(data_path / "raw_tracks_excerpt.csv")
    reader = TrackCSVReader(album_filename, track_filename)
    track_list, album_set, artist_set, genre_set = reader.read_csv_files()
    for track in track_list:
        repo.add_track(track)

def populate(data_path: Path, repo: MemoryRepository, database_mode: bool):
    load_tracks(data_path, repo, database_mode)


