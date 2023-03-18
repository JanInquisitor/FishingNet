import flask
from flask import render_template

blueprint = flask.Blueprint('package', __name__, template_folder='templates')


@blueprint.route('/test')
def test_route():
    # When you send dictionaries flask sends then as JSON
    return {"message": "this is just a test."}
