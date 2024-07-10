from flask import Flask

from .config import config_app

from .extensions import register_extensions

from .urls import register_urls

from .command import register_commands

app = Flask(__name__)

config_app(app)

register_extensions(app)

register_urls(app)

register_commands(app)
