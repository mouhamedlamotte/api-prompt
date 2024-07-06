import bcrypt
from flask import Blueprint, redirect, request, jsonify, url_for
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

from .authorization.decorators import mail_confirmed_required

from app.lib import db, _send_confirm_email

from constant import FLASK_SECRET_KEY

import jwt


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
        print(user)
        print("user.get('emailverified') ,", user.get("emailverified"))
        if user.get("emailverified") == False:
            return jsonify({
                "success": -1,
                "msg": "Unauthorized, please verify your email first"}), 401
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
@mail_confirmed_required
def me():
    email = get_jwt_identity()
    user = db.get_user_by_email(email)
    return user

@auth_bp.route("/confirm-email", methods=["GET"])
def confirm_email():
    try :
        token = request.args.get("token")
        success_redirect = request.args.get("success_redirect")
        failure_redirect = request.args.get("failure_redirect")
        print(token)
        decoded_token = jwt.decode(token, FLASK_SECRET_KEY, algorithms=["HS256"])
        print(decoded_token)
        email = decoded_token['sub']
        print(email)
        res = db.confirm_email(email)
        if res == False :
            return redirect(failure_redirect)
        return redirect(success_redirect)
    except jwt.ExpiredSignatureError:
        return "<h2>Ce lien a expire</h2>"
    except Exception as e :
        print("Une erreur s'est produite dans la fonction confirm_email de la classe auth ==> \n", e)
        return redirect(failure_redirect)


@auth_bp.route("/send_confirmation_email", methods=["POST"])
def send_confirmation_email():
    data = request.get_json()
    if not data.get("email"):
        return jsonify({
            "success": -1,
            "msg": "Email is required"
        }), 400
        
    token = create_access_token(identity=data.get("email"))
    success_redirect = data.get("success_redirect", "/auth/confirm_success")
    failure_redirect = data.get("failure_redirect", "/auth/confirm_failure")
    _send_confirm_email(data, f"http://127.0.0.1:5000/auth/confirm-email?token={token}&success_redirect={success_redirect}&failure_redirect={failure_redirect}")
    return jsonify({
        "success": 1,
        "msg": "Email de confirmation envoye avec success"
    }), 201

@auth_bp.route("/confirm_success")
def confirm_success():
    return "<h2>Email confirme avec success</h2>"

@auth_bp.route("/confirm_failure")
def confirm_failure():
    return "<h2>Une erreur s'est produite , veuillez reesayer</h2>"