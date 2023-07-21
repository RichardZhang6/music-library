from pathlib import Path
from music.adapters.csvdatareader import TrackCSVReader
data_path = Path('data')

album_filename = str(data_path / "raw_albums_excerpt.csv")
track_filename = str(data_path / "raw_tracks_excerpt.csv")
reader = TrackCSVReader(album_filename, track_filename)
track_list, album_set, artist_set, genre_set = reader.read_csv_files()
for genre in track_list:
    print(genre.image_url)
