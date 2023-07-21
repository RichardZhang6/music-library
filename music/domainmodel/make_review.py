# from music.domainmodel.track import Track, Review
# from music.domainmodel.user import User
# #from music.domainmodel.review import Review
from music.domainmodel.model import Track, Review, User
from datetime import date, datetime


def make_review(self, review_text: str, rating: int, user: User, track: Track, timestamp: datetime = datetime.today()):
    review = Review(track, review_text, rating)
    user.add_review(review)
    track.add_review(review)
    return review