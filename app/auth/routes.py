import bcrypt
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

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
    
    if user :
        pw = data.get("password")
        user_pw = user.get("password")
        print(pw)
        print(user_pw)
        check_password = bcrypt.checkpw(pw.encode('utf-8'), user_pw.encode('utf-8'))
        print(check_password)
        if not check_password:
            return jsonify({
                "success": -1,
                "msg": "Wrong email or password"
                }), 401
        return jsonify({
            "success": 1,
            "access_token": create_access_token(identity=data.get("email"))})
    else :
        return jsonify({
            "success": -1,
            "msg": "Wrong email or password"
            }), 401
    
@auth_bp.route("/me", methods=["POST"])
@jwt_required()
def me():
    email = get_jwt_identity()
    user = db.get_user_by_email(email)
    return user
