from pathlib import Path

from music.adapters.repository import AbstractRepository
from music.adapters.csvimporter import load_album, load_artist, load_genre
from music.adapters.memory_repository import load_tracks

def populate(data_path: Path, repo: AbstractRepository, database_mode: bool):
    load_album(data_path, repo, database_mode)
    load_artist(data_path, repo, database_mode)
    load_genre(data_path, repo, database_mode)
    load_tracks(data_path, repo, database_mode)
