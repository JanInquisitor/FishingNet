import os.path

from flask import Flask
from fishingnet.data import db_session as db_session
from fishingnet.views import home_views, account_views
from fishingnet.profile import profile_views
from fishingnet.home import package_views


class EndpointHandler:
    def __init__(self, action):
        self.action = action


class FlaskAppWrapper:
    def __init__(self, flask_app, **configs):
        self.config = flask_app.config
        self.app = flask_app
        self.configs(**configs)

    def configs(self, **configs):
        for config, value in configs:
            self.app.config[config.upper()] = value

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None, methods=['GET'], *args, **kwargs):
        self.app.add_url_rule(endpoint, endpoint_name, handler, methods=methods, *args, **kwargs)

    def run(self, **kwargs):
        self.app.run(**kwargs)

    def register_blueprint(self, bp):
        self.app.register_blueprint(bp)

    def add_url_rule(self, url, view, name, template, methods=None):
        self.app.add_url_rule(url, methods=methods, view_func=view.as_view(name), template='home/index.html')


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'dbsqlite',
        'fishingnet.sqlite')

    db_session.global_init(db_file)


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Super-duper-secret-key'  # This a testing key.

# app.register_blueprint(HomeView.blueprint)
app.add_url_rule("/", view_func=home_views.as_view('home_view'))
app.add_url_rule("/<page>", view_func=home_views.as_view('home_view_page'))
app.register_blueprint(account_views.blueprint)
app.register_blueprint(package_views.blueprint)
app.register_blueprint(profile_views.blueprint)
# app.register_blueprint(cms_views.blueprint)

if __name__ == '__main__':
    setup_db()
app.run(debug=True)
