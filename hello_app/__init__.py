""" Service module init. Register endpoints here"""

from flask import Flask, jsonify
from jwt_authenticator.authentication_handler import AuthError
from .api_v1_0 import api as api_blueprint_v1_0
from .api_v1_1 import api as api_blueprint_v1_1

APP = Flask(__name__)
APP.config.from_object('config')


APP.register_blueprint(api_blueprint_v1_0, url_prefix="/app/v1.0")
APP.register_blueprint(api_blueprint_v1_0, url_prefix="/app/v1.1")


@APP.errorhandler(AuthError)
def handle_auth_error(ex):
    """Authentication error handler for all endpoints"""

    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
