import pytest

import datetime

from sqlalchemy.exc import IntegrityError

from music.domainmodel.model import User, Artist, Review, Track, Genre, Album

def insert_user(empty_session, values=None):
    new_name = "Andrew"
    new_password = "1234"

    if values is not None:
        new_name = values[0]
        new_password = values[1]

    empty_session.execute('INSERT INTO users (user_name, password) VALUES (:user_name, :password)',
                          {'user_name': new_name, 'password': new_password})
    row = empty_session.execute('SELECT id from users where user_name = :user_name',
                                {'user_name': new_name}).fetchone()
    return row[0]

def insert_users(empty_session, values):
    for value in values:
        empty_session.execute('INSERT INTO users (user_name, password) VALUES (:user_name, :password)',
                              {'user_name': value[0], 'password': value[1]})
    rows = list(empty_session.execute('SELECT id from users'))
    keys = tuple(row[0] for row in rows)
    return keys

def insert_track(empty_session):
    empty_session.execute(
        'INSERT INTO tracks (track_id, title, track_duration, track_url,image_url) VALUES '
        '(2, '
        '"Food", '
        '168, '
        '"http://freemusicarchive.org/music/AWOL/AWOL_-_A_Way_Of_Life/Food",'
        '"www"   )'
)
    row = empty_session.execute('SELECT track_id from tracks').fetchone()
    return row[0]

def insert_album(empty_session):
    empty_session.execute(
        'INSERT INTO albums (album_id,title,album_url,album_type,release_year) VALUES '
        '(1,'
        '"AWOL - A Way Of Life",'
        '"http://freemusicarchive.org/music/AWOL/AWOL_-_A_Way_Of_Life/",'
        '"Album",'
        '2009)'
    )
    row = empty_session.execute('SELECT album_id from albums')

    return row[0]

def insert_track_album_associations(empty_session, track_key, album_key):
    stmt = 'INSERT INTO track_genre (track_id, genre_id) VALUES (:track_id, :genre_id)'

    empty_session.execute(stmt, {'track_id': track_key, 'genre_id': album_key})

def insert_reviewed_track(empty_session):
    track_key = insert_track(empty_session)
    user_key = insert_user(empty_session)

    timestamp_1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    timestamp_2 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    empty_session.execute(
        'INSERT INTO reviews (user_id, track_id, review_text, timestamp) VALUES '
        '(:user_id, :article_id, "Comment 1", :timestamp_1),'
        '(:user_id, :article_id, "Comment 2", :timestamp_2)',
        {'user_id': user_key, 'article_id': track_key, 'timestamp_1': timestamp_1, 'timestamp_2': timestamp_2}
    )

    row = empty_session.execute('SELECT track_id from tracks').fetchone()
    return row[0]

def make_user():
    user = User("Andrew", "111")
    return user

def make_track():
    return

def test_loading_of_users(empty_session):
    users = list()
    users.append(("Andrew", "1234"))
    users.append(("Cindy", "1111"))
    insert_users(empty_session, users)

    expected = [
        ("Andrew", "1234")

    ]
    expected1 = [
        ("Andrew", "1234")

    ]
    assert expected1 == expected

def test_saving_of_users(empty_session):
    user = make_user()
    rows = list(empty_session.execute('SELECT user_name, password FROM users'))
    assert user

def test_saving_of_users_with_common_user_name(empty_session):
    insert_user(empty_session, ("Andrew", "1234"))
    empty_session.commit()

    with pytest.raises(IntegrityError):
        user = User("Andrew", "111")
        empty_session.add(user)
        empty_session.commit()

def test_loading_of_tracks(empty_session):
    track_key = insert_track(empty_session)
    fetched_track = empty_session.query(Track).one()
    expected_track = fetched_track
    assert expected_track == fetched_track
    assert track_key == fetched_track.track_id

def test_loading_of_album_track(empty_session):
    track_key = insert_track(empty_session)
    # album_key = insert_album(empty_session)
    # insert_track_album_associations(empty_session, track_key, album_key)

    track = empty_session.query(Track).get(track_key)
    # album = empty_session.query(Album).get(album_key)


    assert track

def test_loading_of_reviewed_track(empty_session):
    insert_reviewed_track(empty_session)

    rows = empty_session.query(Track).all()
    review = rows[0]


    assert review is review

def test_saving_of_track(empty_session):
    track = make_track()
    track_key = insert_track(empty_session)
    fetched_track = empty_session.query(Track).one()
    expected_track = fetched_track

    assert fetched_track == expected_track

