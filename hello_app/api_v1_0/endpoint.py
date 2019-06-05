from jwt_authenticator.authentication_handler import AuthenticationHandler
from . import api
from flask import g


@api.route('/', methods=['GET'])
def get_all():
    return "Hello, World!"


@api.route('/<name>', methods=['GET'])
@AuthenticationHandler.requires_auth("user")
def get_one(name):
    return f"Hello {name}. Your claims are {g.current_user}"

