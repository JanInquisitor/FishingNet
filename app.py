import os.path
from flask import Flask

from fishingnet.data import db_session as db_session
from fishingnet.authentication import account_views
from fishingnet.profile import profile_views
from fishingnet.home.home_views import HomeView
from fishingnet.wiki.wiki_views import WikiView
from fishingnet.authentication.account_views import AccountIndexView, RegisterView, LoginView


class FlaskAppWrapper:
    def __init__(self, app_name, config_secret_key, **configs):
        self.app = Flask(app_name)
        self.app.config['SECRET_KEY'] = config_secret_key

        self.configs(**configs)
        self.setup_db()
        self.register_blueprints()
        # self.add_url_rules()
        self.add_url_rules_set([
            ("/", HomeView, "home_view"),
            ("/<page>", HomeView, "home_view_page"),
            ("/wiki", WikiView, 'wiki_view'),
            ("/account", AccountIndexView, "account_index"),
            ("/account/register", RegisterView, "register"),
            ("/account/login", LoginView, "login")

        ])

    def configs(self, **configs):
        for config, value in configs.items():
            self.app.config[config.upper()] = value

    def setup_db(self):
        db_file = os.path.join(
            os.path.dirname(__file__),
            'dbsqlite',
            'fishingnet.sqlite'
        )
        db_session.global_init(db_file)

    def register_blueprints(self):
        # self.app.register_blueprint(account_views.blueprint)
        self.app.register_blueprint(profile_views.blueprint)

    def add_url_rules(self):
        # Add URL rules for class-based views here
        self.add_view_rule(HomeView, '/', 'home_view')
        self.add_view_rule(HomeView, '/<page>', 'home_view_page')
        self.add_view_rule(WikiView, '/wiki', 'wiki_view')

    def add_view_rule(self, view_class, url, name):
        view_func = view_class.as_view(name)
        self.app.add_url_rule(url, view_func=view_func)

    def add_url_rules_set(self, url_rules):
        for rule, view_class, endpoint in url_rules:
            self.app.add_url_rule(rule, view_func=view_class.as_view(endpoint))

    def run(self, **kwargs):
        self.app.run(**kwargs)


if __name__ == '__main__':
    app_name = __name__
    secret_key = 'Super-duper-secret-key'  # This is a testing key.
    app_wrapper = FlaskAppWrapper(app_name, secret_key, DEBUG=True)
    app_wrapper.run(debug=True)
