from jwt_authenticator.authentication_handler import AuthenticationHandler
from . import api


@api.route('/', methods=['GET'])
def get_all():
    return "Hello, World!"


@api.route('/<name>', methods=['GET'])
@AuthenticationHandler.requires_auth("admin")
def get_one(name):
    return f"Hello {name}"

