import bcrypt
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

from app.lib import db


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/token", methods=["POST"])
def token():
    data = request.get_json()
    if not data.get("email") or not data.get("password"):
        return jsonify({
            "success": -1,
            "msg": "Email and password are required"
            
            }), 400
    user = db.get_user_by_email(data.get("email"))
    check_password = bcrypt.checkpw(data.get("password").encode('utf8'), user.get("password").encode('utf8'))
    if not user or not check_password:
        return jsonify({
            "success": -1,
            "msg": "Wrong email or password"
            }), 401
    return jsonify({
        "success": 1,
        "access_token": create_access_token(identity=data.get("email"))})