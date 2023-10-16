from flask import render_template, request, redirect, url_for
from flask.views import View, MethodView
from fishingnet.fish.fish_service import FishService


class FishView(MethodView):
    service = FishService()

    def get(self):
        fish_info = self.service.create_fish()
        return render_template("/fish/detail.html", fish_info=fish_info)


class FishAddView(MethodView):
    service = FishService()

    def get(self):
        # Render the fish add form
        return render_template("/fish/add.html")

    def post(self):
        name = request.form.get("name")
        email = request.form.get("email")
        description = request.form.get("description")

        # Use the form data to create a new fish
        fish_info = self.service.create_fish(name, email, description)

        # Redirect to the updated fish detail page
        return render_template("/fish/add.html")  # Render the form page


class FishFeed(View):
    def dispatch_request(self):
        return render_template("/fish/feed.html")
