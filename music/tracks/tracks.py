from datetime import date
from flask import Blueprint
from flask import request, render_template, redirect, url_for, session

from flask_wtf import FlaskForm
from wtforms import TextAreaField, HiddenField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, ValidationError

import music.adapters.repository as repo
import music.tracks.services as services
from music.authentication.authentication import login_required


tracks_blueprint = Blueprint('tracks_bp', __name__)

@tracks_blueprint.route('/track_by_id', methods=['GET'])
def track_by_id():
    track_id = int(request.args.get('id'))
    review = request.args.get('view_review_for')
    if review is None:
        review = -1
    else:
        review = int(review)
    track = services.get_track_by_id(track_id, repo.repo_instance)
    track.view_review_url = url_for('tracks_bp.track_by_id', id = track_id, view_review_for = track_id)
    track.add_review_url = url_for('tracks_bp.review_on_track', id = track_id)
    return render_template('tracks/track_details.html',
                           track = track,
                           view_review_url = track.view_review_url,
                           add_review_url = track.add_review_url,
                           review = review)




@tracks_blueprint.route('/tracks_by_page', methods=['GET'])
def tracks_by_page():
    num = int(request.args.get('page'))

    first_page = services.get_first_page(repo.repo_instance)
    last_page = services.get_last_page(repo.repo_instance)
    tracks, prev_page, next_page = services.get_tracks_by_page(num, repo.repo_instance)

    if num > 0 and num < last_page:
        prev_page_url = url_for('tracks_bp.tracks_by_page', page = prev_page)
        first_page_url = url_for('tracks_bp.tracks_by_page', page = first_page)
            #if next_page is not None:
        next_page_url = url_for('tracks_bp.tracks_by_page', page = next_page)
        last_page_url = url_for('tracks_bp.tracks_by_page', page = last_page)
    elif num >= last_page:
        prev_page_url = url_for('tracks_bp.tracks_by_page', page=prev_page)
        first_page_url = url_for('tracks_bp.tracks_by_page', page=first_page)
        # if next_page is not None:
        next_page_url = url_for('tracks_bp.tracks_by_page', page=last_page)
        last_page_url = url_for('tracks_bp.tracks_by_page', page=last_page)
    elif num <= 0:
        prev_page_url = url_for('tracks_bp.tracks_by_page', page=first_page)
        first_page_url = url_for('tracks_bp.tracks_by_page', page=first_page)
        # if next_page is not None:
        next_page_url = url_for('tracks_bp.tracks_by_page', page=next_page)
        last_page_url = url_for('tracks_bp.tracks_by_page', page=last_page)

    return render_template('simple_track.html',
                               tracks = tracks,
                               first_page_url = first_page_url,
                               last_page_url = last_page_url,
                               next_page_url = next_page_url,
                               prev_page_url = prev_page_url
                               )



@tracks_blueprint.route('/review', methods=['GET', 'POST'])
@login_required
def review_on_track():
    user_name = session['user_name']

    form = ReviewForm()

    if form.validate_on_submit():
        track_id = int(form.track_id.data)

        services.add_review(track_id, form.review.data, form.rating.data, user_name, repo.repo_instance)

        #track = services.get_track_by_id(track_id, repo.repo_instance)

        return redirect(url_for('tracks_bp.track_by_id', id=track_id, view_review_for = track_id))

    if request.method == 'GET':
        track_id = int(request.args.get('id'))
        form.track_id.data = track_id
    else:
        track_id = int(form.track_id.data)

    track = services.get_track_by_id(track_id, repo.repo_instance)
    return render_template(
        'tracks/reviews.html',
        track = track,
        form=form,
        handler_url=url_for('tracks_bp.review_on_track', id=track_id)
    )

@tracks_blueprint.route('/tracks_by_artist', methods=['GET'])
def tracks_by_artist():
    artist_name = request.args.get('name')
    tracks = services.get_track_by_artist(artist_name, repo.repo_instance)
    return render_template('tracks/by_artist.html',
                           tracks = tracks,
                           search = artist_name)

@tracks_blueprint.route('/tracks_by_album', methods=['GET'])
def tracks_by_album():
    album_name = request.args.get('name')
    tracks = services.get_tracks_by_album(album_name, repo.repo_instance)
    return render_template('tracks/by_album.html',
                           tracks = tracks,
                           search = album_name)

@tracks_blueprint.route('/tracks_by_genre', methods=['GET'])
def tracks_by_genre():
    genre_type = request.args.get('type')
    tracks = services.get_tracks_by_genre(genre_type, repo.repo_instance)
    return render_template('tracks/by_genre.html',
                           tracks = tracks,
                           search = genre_type)


class ReviewForm(FlaskForm):
    review = TextAreaField('Review', [
        DataRequired(),
        Length(min=4, message='Your comment is too short')])
    rating = IntegerField('Rating',[DataRequired()])
    track_id = HiddenField("Track id")
    submit = SubmitField('Submit')
    #ProfanityFree(message='Your comment must not contain profanity')