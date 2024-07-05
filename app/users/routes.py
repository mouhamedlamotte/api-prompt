import bcrypt

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.auth.authorization.decorators import superuser_required
from app.lib import db, send_email



user_bp = Blueprint("users", __name__)


@user_bp.route("/users", methods=["GET"])
@jwt_required()
@superuser_required
def get_users():
    users = db.get_data_table("users")
    return jsonify(users), 200

@user_bp.route("/users", methods=["POST"])
def create_user():
    try :
        data =  request.get_json()
        if not data.get("email") and not data.get("password"):
            return jsonify({
                "success" : -1,
                "msg" : "veuillez fournir un email et un mot de passe",
            }), 403
        pw = data.get("password")
        hashed_pw = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        data["password"] = hashed_pw
        res, msg = db.create_user(**data)
        if res == False :
            return jsonify({
                "success" : -1,
                "msg" : msg,
            }), 403
        send_email(data, "http://127.0.0.1:5000/confirm-email")
        return jsonify(
            {
                "success" : 1,
                "msg" : f"l'utilisateur {data.get('email')} a ete cree avec success",
            }
        ), 201
    except Exception as e :
        print("Une erreur s'est produite dans la fonction create_user de la route users ==> \n", e)
        return jsonify({
                "success" : -1,
                "msg" : "Une erreur s'est produite , veuillez reesayer",
        }), 500
        
        
