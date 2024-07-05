from datetime import timedelta
from dotenv import load_dotenv

from constant import FLASK_SECRET_KEY

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager



from .users.routes import user_bp
from .auth.routes import auth_bp
from .prompts.routes import prompt_bp
from .group.routes import group_bp
from app.lib.postgres import Postgres

db = Postgres()

import click

load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = FLASK_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)

CORS(app)

jwt = JWTManager(app)

app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(prompt_bp, url_prefix="/prompts")
app.register_blueprint(group_bp, url_prefix="/groups")




with app.app_context():
    @click.command('init-db')
    def init_db_command():
        db.init_db()
        click.echo('Initialized the database.')
    app.cli.add_command(init_db_command)