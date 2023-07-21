from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship, synonym

# from music.domainmodel.artist import Artist
# from music.domainmodel.album import Album
# from music.domainmodel.track import Track,Review
# from music.domainmodel.genre import Genre
# from music.domainmodel.user import User
from music.domainmodel.model import Album, Artist, Track, Review, Genre, User

metadata = MetaData()
track_table=Table(
    'tracks',metadata,
    Column('track_id', Integer, primary_key=True),
    Column('track_title', String(255), nullable=False),
    Column('track_duration', Integer),
    Column('track_url',String(1024)),
    Column('album_id', ForeignKey('albums.album_id')),
    Column('artist_id', ForeignKey('artists.artist_id')),
    Column('image_url',String(1024))
)
users_table = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_name', String(255), unique=True, nullable=False),
    Column('password', String(255), nullable=False)
)
reviews_table = Table(
    'reviews', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('user_id', ForeignKey('users.id')),
    Column('track_id', ForeignKey('tracks.track_id')),
    Column('review_text', String(1024), nullable=False),
    Column('timestamp', DateTime, nullable=False)
)
albums_table=Table(
    'albums',metadata,
    Column('album_id', Integer, primary_key=True),
    # Column('track_id', ForeignKey('tracks.track_id')),
    Column('title',String(255),nullable=False),
    Column('album_url', String(1024)),
    Column('album_type', String(255)),
    Column('release_year', Integer)
)
artists_table=Table(
    'artists',metadata,
    Column('artist_id',Integer,primary_key=True),
    # Column('track_id', ForeignKey('tracks.track_id')),
    Column('full_name',String(1024),nullable=False)
)
genre_table=Table(
    'genres',metadata,
    #Column('id',Integer,primary_key=True,autoincrement=True),
    Column('genre_id',Integer, primary_key = True),
    Column('name',String(1024), nullable=False)
)

# track_album_table = Table(
#     'track_album',metadata,
#     Column('id',Integer,primary_key=True,autoincrement=True),
#     Column('track_id',ForeignKey('tracks.track_id')),
#     Column('album_id',ForeignKey('albums.album_id'))
# )
#
# track_artist_table = Table(
#     'track_artist',metadata,
#     Column('id',Integer,primary_key=True,autoincrement=True),
#     Column('track_id',ForeignKey('tracks.track_id')),
#     Column('artist_id',ForeignKey('artists.artist_id'))
# )

track_genre_table = Table(
    'track_genre', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('track_id', ForeignKey('tracks.track_id')),
    Column('genre_id', ForeignKey('genres.genre_id'))
)
def map_model_to_tables():
    mapper(User, users_table, properties={
        '_User__user_name': users_table.c.user_name,
        '_User__password': users_table.c.password,
        '_User__reviews': relationship(Review, backref='_Review__user')
    })
    mapper(Review, reviews_table, properties={
            '_Review__review_text': reviews_table.c.review_text,
            '_Review__timestamp': reviews_table.c.timestamp
        })
    mapper(Track,track_table,properties={
        '_Track__track_id':track_table.c.track_id,
        '_Track__track_title':track_table.c.track_title,
        '_Track__track_duration':track_table.c.track_duration,
        '_Track__track_url':track_table.c.track_url,
        '_Track__image_url': track_table.c.image_url,
        '_Track__reviews':relationship(Review, backref='_Review__track'),
        '_Track__artist': relationship(Artist, backref="tracks"),
        '_Track__album': relationship(Album, backref="tracks"),
        '_Track__genres': relationship(Genre, secondary=track_genre_table, back_populates='_Genre__tracks')
    })
    mapper(Album, albums_table, properties={
        '_Album__album_id':albums_table.c.album_id,
        '_Album__title':albums_table.c.title,
        '_Album__album_url':albums_table.c.album_url,
        '_Album__album_type':albums_table.c.album_type,
        '_Album__release_year':albums_table.c.release_year
    })
    mapper(Artist, artists_table, properties={
        '_Artist__artist_id':artists_table.c.artist_id,
        '_Artist__full_name':artists_table.c.full_name
    })
    mapper(Genre, genre_table, properties={
        '_Genre__genre_id':genre_table.c.genre_id,
        '_Genre__name':genre_table.c.name,
        '_Genre__tracks': relationship(Track, secondary=track_genre_table, back_populates='_Track__genres')
    })