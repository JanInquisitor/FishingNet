import flask
from flask import render_template
from flask.views import MethodView

from fishingnet.services.package_service import packages

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
def index():
    info_test = {"first": packages(), "second": [1, 2, 3, 4, 5, 6, 7]}
    return render_template('home/index.html', fish_info=info_test)


@blueprint.route('/about')
def about():
    return render_template('home/about.html')


@blueprint.route('/wiki')
def wiki_index():
    return render_template('wiki/wiki.html')



class HomeView(MethodView):
    def get(self, page=None):
        if page == 'about':
            return self.about()
        elif page == 'wiki':
            return self.wiki_index()
        else:
            info_test = {"first": packages(), "second": [1, 2, 3, 4, 5, 6, 7]}
            return render_template('home/index.html', fish_info=info_test)

    def about(self):
        return render_template('home/about.html')

    def wiki_index(self):
        return render_template('wiki/wiki.html')

