from flask import render_template, typing as ft
from flask.views import View, MethodView

from fishingnet.fish.fish_service import FishService


class FishView(MethodView):
    service = FishService()

    # right now this creates the fish but later it will fetch one from the database
    def get(self):
        fish_info = self.service.create_fish()
        return render_template("/fish/fish_detail.html", fish_info=fish_info)

    def post(self):
        pass


class FishFeed(View):

    def dispatch_request(self):
        return render_template("/fish/feed.html")
