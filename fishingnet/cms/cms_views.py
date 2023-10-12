import flask
from flask import render_template
from flask.views import View

from fishingnet.cms import cms_service

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')


@blueprint.route('/<path:url>')
def cms_page(url: str):
    page = cms_service.get_page(url)
    if not page:
        return flask.abort(404)
    return render_template('cms/page.html', page=page)


class CMSViews(View):
    methods = ["GET", "POST"]

    def __init__(self, model, template):
        self.model = model
        self.template = template
        self.cms_service = cms_service()

    def get(self):
        page = self.cms_service.get_page(url)
        if not page:
            return flask.abort(404)
        return render_template('cms/page.html', page=page)

    def dispatch_request(self):
        pass
