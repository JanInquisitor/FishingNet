from flask import render_template, request
from flask.views import MethodView

from fishingnet.fish.fish_service import FishService
from fishingnet.services.package_service import packages


class HomeView(MethodView):
    def get(self, page=None):
        if page == 'about':
            return self.about()
        else:
            service = FishService()
            count = service.count_all_fish()
            return render_template('home/index.html', count=count)

    def about(self):
        return render_template('home/about.html')

    def wiki(self):
        return render_template('wiki/wiki.html')
