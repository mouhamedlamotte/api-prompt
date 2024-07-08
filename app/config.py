from datetime import timedelta

from constant import FLASK_SECRET_KEY, GMAIL_STMP_PW, GMAIL_STMP_USERNAME



class Config:
    SECRET_KEY = FLASK_SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = GMAIL_STMP_USERNAME
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PASSWORD = GMAIL_STMP_PW
    

def config_app(app):
    app.config.from_object(Config)