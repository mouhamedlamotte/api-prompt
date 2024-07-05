from datetime import timedelta
from dotenv import load_dotenv

from constant import FLASK_SECRET_KEY

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager



from .users import user_bp
from .auth import auth_bp
from .prompts import prompt_bp
from .group import group_bp


from .command import init_db_command, migrate_command




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
    app.cli.add_command(init_db_command)
    app.cli.add_command(migrate_command)
    