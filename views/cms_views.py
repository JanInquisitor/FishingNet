import flask
from flask import render_template
from services.cms_service import get_page

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')


@blueprint.route('/<path:url>')
def cms_page(url: str):
    page = get_page(url)
    if not page:
        return flask.abort(404)
    return render_template('cms/page.html', page=page)
