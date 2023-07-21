import csv
from pathlib import Path
from datetime import date, datetime

from werkzeug.security import generate_password_hash

from music.adapters.repository import AbstractRepository
from music.adapters.csvdatareader import TrackCSVReader
# from music.domainmodel.artist import Artist
# from music.domainmodel.album import Album
# from music.domainmodel.track import Track
# from music.domainmodel.genre import Genre

def load_artist(data_path: Path, repo: AbstractRepository, database_mode:bool):
    album_filename = str(data_path / "raw_albums_excerpt.csv")
    track_filename = str(data_path / "raw_tracks_excerpt.csv")
    reader = TrackCSVReader(album_filename, track_filename)
    track_list, album_set, artist_set, genre_set = reader.read_csv_files()
    for artist in artist_set:
        repo.add_artist(artist)

def load_album(data_path: Path, repo: AbstractRepository, database_mode: bool):
    album_filename = str(data_path / "raw_albums_excerpt.csv")
    track_filename = str(data_path / "raw_tracks_excerpt.csv")
    reader = TrackCSVReader(album_filename, track_filename)
    track_list, album_set, artist_set, genre_set = reader.read_csv_files()
    for album in album_set:
        repo.add_album(album)


def load_genre(data_path: Path, repo: AbstractRepository, database_mode:bool):
    album_filename = str(data_path / "raw_albums_excerpt.csv")
    track_filename = str(data_path / "raw_tracks_excerpt.csv")
    reader = TrackCSVReader(album_filename, track_filename)
    track_list, album_set, artist_set, genre_set = reader.read_csv_files()
    for genre in genre_set:
        repo.add_genre(genre)
