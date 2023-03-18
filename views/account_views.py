import flask
from flask import render_template, request, redirect

from infrastructure import cookie_auth
from services import user_service

blueprint = flask.Blueprint('account', __name__, template_folder='templates')


@blueprint.route('/account', methods=['GET'])
def index():
    return render_template('account/index.html')


@blueprint.route('/account/register', methods=['GET'])
def register_get():
    return render_template('account/register.html')


@blueprint.route('/account/register', methods=['POST'])
def register_post():
    r = flask.request
    name = r.form.get('name')
    email = r.form.get('email', '').lower().strip()
    password = r.form.get('password')

    if not name or not email or not password:
        return {'error': 'Some require fields are missing.'}

    user = user_service.create_user(name, email, password)
    if not user:
        return {
            'error': 'A user with that email already exists.'
        }

    response = redirect('')
    cookie_auth.set_auth(response, user.id)
    return response  # should redirect to '/me'


@blueprint.route('/account/login', methods=['GET'])
def login_get():
    return render_template('account/login.html')


@blueprint.route('/account/login', methods=['POST'])
def login_post():
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

    user = user_service.login_user(email, password)

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
