from flask import render_template, logging
from flask.views import View, MethodView


class WikiView(View):
    def dispatch_request(self):
        print('Calling wiki')
        return render_template('wiki/wiki.html')
