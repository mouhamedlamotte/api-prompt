from datetime import timedelta
from dotenv import load_dotenv

from constant import FLASK_SECRET_KEY, GMAIL_STMP_PW, GMAIL_STMP_USERNAME

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager





from .users import user_bp
from .auth import auth_bp
from .prompts import prompt_bp
from .group import group_bp


from .command import init_db_command, migrate_command

from .lib import mail



load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = FLASK_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = GMAIL_STMP_USERNAME
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_PASSWORD'] = GMAIL_STMP_PW
 
CORS(app)

jwt = JWTManager(app)
mail.init_app(app)

app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(prompt_bp, url_prefix="/prompts")
app.register_blueprint(group_bp, url_prefix="/groups")




app.cli.add_command(init_db_command)
app.cli.add_command(migrate_command)