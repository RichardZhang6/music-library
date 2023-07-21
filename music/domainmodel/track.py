# from music.domainmodel.artist import Artist
# from music.domainmodel.genre import Genre
# from music.domainmodel.album import Album
# #from music.domainmodel.review import Review
# from datetime import datetime



# class Track:
#     def __init__(self, track_id: int, track_title: str):
#         if type(track_id) is not int or track_id < 0:
#             raise ValueError
#         self.__track_id = track_id
#
#         self.__title = None
#         if type(track_title) is str:
#             self.__title = track_title.strip()
#
#         self.__artist = None
#         self.__album = None
#         self.__track_url: str | None = None
#         # duration in seconds
#         self.__track_duration: int | None = None
#         self.__genres: list = []
#         self.__reviews = list()
#         self.__view_review_url: str | None = None
#         self.__add_review_url: str | None = None
#
#     @property
#     def view_review_url(self) -> str:
#         return self.__view_review_url
#
#     @property
#     def add_review_url(self) -> str:
#         return self.__add_review_url
#
#     @property
#     def reviews(self):
#         return self.__reviews
#
#     @view_review_url.setter
#     def view_review_url(self, url: str):
#         self.__view_review_url = url
#
#     @add_review_url.setter
#     def add_review_url(self, url: str):
#         self.__add_review_url = url
#
#     @property
#     def track_id(self) -> int:
#         return self.__track_id
#
#     @property
#     def title(self) -> str:
#         return self.__title
#
#     @title.setter
#     def title(self, book_title: str):
#         self.__title = None
#         if type(book_title) is str and book_title.strip() != '':
#             self.__title = book_title.strip()
#
#     @property
#     def artist(self) -> Artist:
#         return self.__artist
#
#     @artist.setter
#     def artist(self, new_artist):
#         if isinstance(new_artist, Artist):
#             self.__artist = new_artist
#         else:
#             self.__artist = None
#
#     @property
#     def album(self) -> Album:
#         return self.__album
#
#     @album.setter
#     def album(self, new_album):
#         if isinstance(new_album, Album):
#             self.__album = new_album
#         else:
#             self.__album = None
#
#     @property
#     def track_url(self) -> str:
#         return self.__track_url
#
#     @track_url.setter
#     def track_url(self, new_track_url: str):
#         if type(new_track_url) is str:
#             self.__track_url = new_track_url.strip()
#         else:
#             self.__track_url = None
#
#     @property
#     def track_duration(self) -> int:
#         return self.__track_duration
#
#     @track_duration.setter
#     def track_duration(self, new_duration: int):
#         self.__track_duration = None
#         if type(new_duration) is int and new_duration >= 0:
#             self.__track_duration = new_duration
#         else:
#             raise ValueError
#
#     @property
#     def genres(self) -> list:
#         return self.__genres
#
#     def add_genre(self, new_genre):
#         if not isinstance(new_genre, Genre) or new_genre in self.__genres:
#             return
#         self.__genres.append(new_genre)
#
#     def add_review(self, review):
#         if not isinstance(review, Review) and review in self.__reviews:
#             return
#         self.__reviews.append(review)
#
#
#     def __repr__(self):
#         return f"<Track {self.title}, track id = {self.track_id}>"
#
#     def __eq__(self, other):
#         if not isinstance(other, self.__class__):
#             return False
#         return self.track_id == other.track_id
#
#     def __lt__(self, other):
#         if not isinstance(other, self.__class__):
#             return True
#         return self.track_id < other.track_id
#
#     def __hash__(self):
#         return hash(self.track_id)
#
# class Review:
#
#     def __init__(self, track: Track, review_text: str, rating: int):
#         self.__track = None
#         if isinstance(track, Track):
#             self.__track = track
#
#         self.__review_text = 'N/A'
#         if isinstance(review_text, str):
#             self.__review_text = review_text.strip()
#
#         if isinstance(rating, int) and 1 <= rating <= 5:
#             self.__rating = rating
#         else:
#             raise ValueError('Invalid value for the rating.')
#
#         self.__timestamp = datetime.now()
#
#     @property
#     def track(self) -> Track:
#         return self.__track
#
#     @property
#     def review_text(self) -> str:
#         return self.__review_text
#
#     @review_text.setter
#     def review_text(self, new_text):
#         if type(new_text) is str:
#             self.__review_text = new_text.strip()
#         else:
#             self.__review_text = None
#
#     @property
#     def rating(self) -> int:
#         return self.__rating
#
#     @rating.setter
#     def rating(self, new_rating: int):
#         if isinstance(new_rating, int) and 1 <= new_rating <= 5:
#             self.__rating = new_rating
#         else:
#             self.__rating = None
#             raise ValueError("Wrong value for the rating")
#
#     @property
#     def timestamp(self) -> datetime:
#         return self.__timestamp
#
#     def __eq__(self, other):
#         if not isinstance(other, self.__class__):
#             return False
#         return other.track == self.track and other.review_text == self.review_text and other.rating == self.rating and other.timestamp == self.timestamp
#
#     def __repr__(self):
#         return f'<Review of track {self.track}, rating = {self.rating}, review_text = {self.review_text}>'
