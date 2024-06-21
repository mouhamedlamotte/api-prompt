from datetime import timedelta
import os
from dotenv import load_dotenv

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required

from app.auth.authorization.decorators import staff_required, superuser_required


from .users.routes import user_bp
from .auth.routes import auth_bp


load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("FLASK_SECRET_KEY")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=5)
CORS(app)
jwt = JWTManager(app)

app.register_blueprint(user_bp)
app.register_blueprint(auth_bp)

@app.route("/superuser")
@jwt_required()
@superuser_required  
def superuser():
    return "You are seeing this because you are a superuser"

@app.route("/staff")
@jwt_required()
@staff_required
def staff():
    return get_jwt_identity()