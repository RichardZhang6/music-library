from sqlalchemy import select, inspect
from music.adapters.orm import metadata

def test_database_populate_inspect_table_names(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    assert inspector.get_table_names() == ['albums', 'artists', 'genres', 'reviews', 'track_genre', 'tracks', 'users']

def test_database_populate_select_all_tracks(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_track_table = inspector.get_table_names()[5]

    with database_engine.connect() as connection:
        # query for records in table articles
        select_statement = select([metadata.tables[name_of_track_table]])
        result = connection.execute(select_statement)

        all_tracks = []
        for row in result:
            all_tracks.append((row['track_id'], row['title']))

        nr_tracks = len(all_tracks)
        assert nr_tracks == 2000

        assert all_tracks[0] == (2, 'Food')

def test_database_populate_select_all_users(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_users_table = inspector.get_table_names()[6]

    with database_engine.connect() as connection:
        # query for records in table users
        select_statement = select([metadata.tables[name_of_users_table]])
        result = connection.execute(select_statement)

        all_users = []
        for row in result:
            all_users.append(row['user_name'])

        assert all_users == all_users

def test_database_populate_select_all_albums(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_albums_table = inspector.get_table_names()[0]

    with database_engine.connect() as connection:
        # query for records in table comments
        select_statement = select([metadata.tables[name_of_albums_table]])
        result = connection.execute(select_statement)

        all_albums = []
        for row in result:
            all_albums.append((row['album_id'], row['title']))
        numberalbums=len(all_albums)
        assert numberalbums==427
        assert all_albums[0] == (1, 'AWOL - A Way Of Life')

def test_database_populate_select_all_genres(database_engine):

    # Get table information
    inspector = inspect(database_engine)
    name_of_genre_table = inspector.get_table_names()[2]

    with database_engine.connect() as connection:
        # query for records in table articles
        select_statement = select([metadata.tables[name_of_genre_table]])
        result = connection.execute(select_statement)

        all_genres = []
        for row in result:
            all_genres.append((row['genre_id'], row['name']))

        nr_genres = len(all_genres)
        assert nr_genres == 60

        assert all_genres[0] == (1, 'Avant-Garde')




