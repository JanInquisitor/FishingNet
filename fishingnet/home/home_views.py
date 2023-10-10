from flask import render_template, request
from flask.views import MethodView
from fishingnet.services.package_service import packages


class HomeView(MethodView):
    def get(self, page=None):
        if page == 'about':
            return self.about()
        else:
            info_test = {"first": packages(), "second": [1, 2, 3, 4, 5, 6, 7]}
            return render_template('home/index.html', fish_info=info_test)

    def about(self):
        return render_template('home/about.html')

    def wiki(self):
        return render_template('wiki/wiki.html')
