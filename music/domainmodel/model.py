from datetime import datetime

class Artist:

    def __init__(self, artist_id: int, full_name: str):
        if type(artist_id) is not int or artist_id < 0:
            raise ValueError("Arist ID should be a non negative integer!")
        self.__artist_id: int = artist_id

        if type(full_name) is str:
            self.__full_name: str = full_name.strip()
        else:
            self.__full_name = None

        self.__track: Track

    @property
    def track (self):
        return self.__track

    @property
    def artist_id(self) -> int:
        return self.__artist_id

    @property
    def full_name(self) -> str:
        return self.__full_name

    @full_name.setter
    def full_name(self, new_full_name):
        self.__full_name = None

        if type(new_full_name) is str:
            new_full_name = new_full_name.strip()
            if new_full_name != '':
                self.__full_name = new_full_name

    def __repr__(self):
        return f"<Artist {self.full_name}, artist id = {self.artist_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.artist_id == other.artist_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.artist_id < other.artist_id

    def __hash__(self):
        return hash(self.__artist_id)

class Album:

    def __init__(self, album_id: int, title: str):
        if type(album_id) is not int or album_id < 0:
            raise ValueError("Album ID should be a non negative integer!")
        self.__album_id: int = album_id

        if type(title) is str and title.strip() != '':
            self.__title: str = title.strip()
        else:
            self.__title = None
        self.__track: Track
        self.__album_url: str | None = None
        self.__album_type: str | None = None
        self.__release_year: int | None = None

    @property
    def track(self):
        return self.__track

    @property
    def album_id(self) -> int:
        return self.__album_id

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title):
        if type(new_title) is str and new_title.strip() != '':
            self.__title = new_title.strip()
        else:
            self.__title = None

    @property
    def album_url(self) -> str:
        return self.__album_url

    @album_url.setter
    def album_url(self, new_album_url: str):
        if type(new_album_url) is str:
            self.__album_url = new_album_url.strip()
        else:
            self.__album_url = None

    @property
    def album_type(self) -> str:
        return self.__album_type

    @album_type.setter
    def album_type(self, new_album_type: str):
        if type(new_album_type) is str:
            self.__album_type = new_album_type.strip()
        else:
            self.__album_type = None

    @property
    def release_year(self) -> int:
        return self.__release_year

    @release_year.setter
    def release_year(self, new_release_year: int):
        if type(new_release_year) is int and new_release_year >= 0:
            self.__release_year = new_release_year
        else:
            self.__release_year = None

    def __repr__(self) -> str:
        return f"<Album {self.title}, album id = {self.album_id}>"

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.album_id == other.album_id

    def __lt__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return True
        return self.album_id < other.album_id

    def __hash__(self):
        return hash(self.album_id)


class Track:

    def __init__(self, track_id: int, title: str):
        if type(track_id) is not int or track_id < 0:
            raise ValueError
        self.__track_id = track_id

        self.__track_title = None
        if type(title) is str:
            self.__track_title = title.strip()

        self.__artist: Artist
        self.__album: Album
        self.__track_url: str | None = None
        # duration in seconds
        self.__track_duration: int | None = None
        self.__genres: list = []
        self.__reviews = list()
        self.__view_review_url: str | None = None
        self.__add_review_url: str | None = None
        self.__image_url: str | None = None

    @property
    def image_url(self):
        return self.__image_url
    @image_url.setter
    def image_url(self, url: str):
        self.__image_url = url

    @property
    def view_review_url(self) -> str:
        return self.__view_review_url

    @property
    def add_review_url(self) -> str:
        return self.__add_review_url

    @property
    def reviews(self):
        return self.__reviews

    @view_review_url.setter
    def view_review_url(self, url: str):
        self.__view_review_url = url

    @add_review_url.setter
    def add_review_url(self, url: str):
        self.__add_review_url = url

    @property
    def track_id(self) -> int:
        return self.__track_id

    @property
    def track_title(self) -> str:
        return self.__track_title

    @track_title.setter
    def track_title(self, book_title: str):
        self.__track_title = None
        if type(book_title) is str and book_title.strip() != '':
            self.__track_title = book_title.strip()

    @property
    def artist(self) -> Artist:
        return self.__artist

    @artist.setter
    def artist(self, new_artist):
        if isinstance(new_artist, Artist):
            self.__artist = new_artist
        else:
            self.__artist = None

    @property
    def album(self) -> Album:
        return self.__album

    @album.setter
    def album(self, new_album):
        if isinstance(new_album, Album):
            self.__album = new_album
        else:
            self.__album = None

    @property
    def track_url(self) -> str:
        return self.__track_url

    @track_url.setter
    def track_url(self, new_track_url: str):
        if type(new_track_url) is str:
            self.__track_url = new_track_url.strip()
        else:
            self.__track_url = None

    @property
    def track_duration(self) -> int:
        return self.__track_duration

    @track_duration.setter
    def track_duration(self, new_duration: int):
        self.__track_duration = None
        if type(new_duration) is int and new_duration >= 0:
            self.__track_duration = new_duration
        else:
            raise ValueError

    @property
    def genres(self) -> list:
        return self.__genres

    def add_genre(self, new_genre):
        if not isinstance(new_genre, Genre) or new_genre in self.__genres:
            return
        self.__genres.append(new_genre)

    def add_review(self, review):
        if not isinstance(review, Review) and review in self.__reviews:
            return
        self.__reviews.append(review)

    def __repr__(self):
        return f"<Track {self.track_title}, track id = {self.track_id}>"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.track_id == other.track_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.track_id < other.track_id

    def __hash__(self):
        return hash(self.track_id)


class Genre:

    def __init__(self, genre_id: int, genre_name: str):
        if type(genre_id) is not int or genre_id < 0:
            raise ValueError('Genre ID should be an integer!')
        self.__genre_id = genre_id

        if type(genre_name) is str:
            self.__name = genre_name.strip()
        else:
            self.__name = None
        self.__tracks = list()

    @property
    def genre_id(self) -> int:
        return self.__genre_id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = None
        if type(name) is str:
            name = name.strip()
            if name != '':
                self.__name = name

    @property
    def tracks(self):
        return self.__tracks

    def add_track(self, track: Track):
        self.__tracks.append(track)

    def __repr__(self) -> str:
        return f'<Genre {self.name}, genre id = {self.genre_id}>'

    def __eq__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            return False
        return self.genre_id == other.genre_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.genre_id < other.genre_id

    def __hash__(self):
        return hash(self.genre_id)


class Review:

    def __init__(self, track: Track, review_text: str, rating: int):
        self.__track = None
        if isinstance(track, Track):
            self.__track = track

        self.__review_text = 'N/A'
        if isinstance(review_text, str):
            self.__review_text = review_text.strip()

        if isinstance(rating, int) and 1 <= rating <= 5:
            self.__rating = rating
        else:
            raise ValueError('Invalid value for the rating.')

        self.__track: Track
        self.__user: User
        self.__timestamp = datetime.now()

    @property
    def track(self) -> Track:
        return self.__track

    @property
    def user(self):
        return self.__user

    @property
    def review_text(self) -> str:
        return self.__review_text

    @review_text.setter
    def review_text(self, new_text):
        if type(new_text) is str:
            self.__review_text = new_text.strip()
        else:
            self.__review_text = None

    @property
    def rating(self) -> int:
        return self.__rating

    @rating.setter
    def rating(self, new_rating: int):
        if isinstance(new_rating, int) and 1 <= new_rating <= 5:
            self.__rating = new_rating
        else:
            self.__rating = None
            raise ValueError("Wrong value for the rating")

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.track == self.track and other.review_text == self.review_text and other.rating == self.rating and other.timestamp == self.timestamp

    def __repr__(self):
        return f'<Review of track {self.track}, rating = {self.rating}, review_text = {self.review_text}>'


class User:

    def __init__(self, user_name: str, password: str):
        #if type(user_id) is not int or user_id < 0:
            #raise ValueError("User ID should be a non negative integer.")
        #self.__user_id = user_id

        if type(user_name) is str:
            self.__user_name = user_name.lower().strip()
        else:
            self.__user_name = None

        if isinstance(password, str) and len(password) >= 7:
            self.__password = password
        else:
            self.__password = None

        self.__reviews: list[Review] = []
        self.__liked_tracks: list[Track] = []

    #@property
    #def user_id(self) -> int:
        #return self.__user_id

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def reviews(self) -> list:
        return self.__reviews

    def add_review(self, new_review: Review):
        if not isinstance(new_review, Review) or new_review in self.__reviews:
            return
        self.__reviews.append(new_review)

    def remove_review(self, review: Review):
        if not isinstance(review, Review) or review not in self.__reviews:
            return
        self.__reviews.remove(review)

    @property
    def liked_tracks(self) -> list:
        return self.__liked_tracks

    def add_liked_track(self, track: Track):
        if not isinstance(track, Track) or track in self.__liked_tracks:
            return
        self.__liked_tracks.append(track)

    def remove_liked_track(self, track: Track):
        if not isinstance(track, Track) or track not in self.__liked_tracks:
            return
        self.__liked_tracks.remove(track)

    def __repr__(self):
        return f'<User {self.user_name}, user id = {self.user_id}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.user_id == other.user_id

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            return True
        return self.user_id < other.user_id

    def __hash__(self):
        return hash(self.user_id)

