import os.path

from flask import Flask
from data import db_session as db_session
from views import home_views, profile_views, cms_views, account_views
from views import package_views


class EndpointHandler:
    def __init__(self, action):
        self.action = action


class FlaskAppWrapper:
    def __init__(self, app, **configs):
        self.app = app
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


def setup_db():
    db_file = os.path.join(
        os.path.dirname(__file__),
        'dbsqlite',
        'fishingnet.sqlite')

    db_session.global_init(db_file)


flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = 'Super-duper-secret-key' # This a testing key.
app = FlaskAppWrapper(flask_app)

app.register_blueprint(home_views.blueprint)
app.register_blueprint(account_views.blueprint)
app.register_blueprint(package_views.blueprint)
app.register_blueprint(profile_views.blueprint)
app.register_blueprint(cms_views.blueprint)

if __name__ == '__main__':
    setup_db()
    app.run(debug=True)
