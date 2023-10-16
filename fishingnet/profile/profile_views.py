from flask import render_template, request, views
from flask.views import MethodView


class ProfileView(MethodView):
    def get(self):
        profile_id = request.args.get('id')
        if profile_id is not None:
            return f"<h1>This is the profile of {profile_id}<h1>"
        else:
            return "<h1>These are the recently updated profiles<h1>"

    def post(self):
        pass
