import flask
from flask import render_template, request

blueprint = flask.Blueprint('profiles', __name__, template_folder='templates')


@blueprint.route('/profile/<int:profile_id>', methods=['GET'])
def profile_details(profile_id: int):
    return f"<h1>This is the profile of {profile_id}<h1>"


@blueprint.route('/profile/recent', methods=['GET'])
def recently_updated():
    return "<h1>These are the recently updated profiles<h1>"
