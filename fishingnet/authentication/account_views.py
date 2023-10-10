from flask import render_template, request, redirect, Blueprint
from flask.views import MethodView
from fishingnet.infrastructure import cookie_auth
from fishingnet.services.user_service import UserService

account_blueprint = Blueprint('account', __name__, template_folder='templates')


class AccountIndexView(MethodView):
    def get(self):
        return render_template('account/index.html')


class RegisterView(MethodView):
    def get(self):
        return render_template('account/register.html')

    def post(self):
        name = request.form.get('name')
        email = request.form.get('email', '').lower().strip()
        password = request.form.get('password')

        if not name or not email or not password:
            return {'error': 'Some required fields are missing.'}

        user = UserService.create_user(name, email, password)

        if not user:
            return {
                'error': 'A user with that email already exists.'
            }

        response = redirect('')
        cookie_auth.set_auth(response, user.id)
        return response  # should redirect to '/me'


class LoginView(MethodView):
    def get(self):
        return render_template('account/login.html')

    def post(self):
        email = request.form.get('email')
        password = request.form.get('password')

        if not email or not password:
            return {
                'email': email,
                'password': password,
                'request_info': {"message": "It work!", "request": request.form, "secure": request.is_secure,
                                 "path": request.path},
                'error': 'Some required fields are missing'
            }

        user = UserService.login_user(email, password)

        if not user:
            return {
                'email': email,
                'password': password,
                'request_info': {"message": "It work!", "request": request.form, "secure": request.is_secure,
                                 "path": request.path},
                'error': 'The account does not exist or the password is wrong.'
            }
        response = redirect('')
        cookie_auth.set_auth(response, user.id)
        return response  # should redirect to '/me'
