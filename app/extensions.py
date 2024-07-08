from flask_cors import CORS

from flask_jwt_extended import JWTManager

from .lib import mail


def register_extensions(app):
    
    CORS(app)

    jwt = JWTManager(app)

    mail.init_app(app)
