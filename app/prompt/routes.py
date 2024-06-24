import base64
import hashlib
import bcrypt

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.auth.authorization.decorators import staff_required
from app.lib import db



prompt_bp = Blueprint("prompt", __name__)


@prompt_bp.route("/prompt", methods=["POST"])
def createPrompt():
    try :
        data =  request.get_json()
        if not data.get("title") and not data.get("text"),:
            return jsonify({
                "success" : -1,
                "msg" : "veuillez fournir un nom et une description",
            }), 403
        res, msg = db.create_prompt(**data)
        if res == False :
            return jsonify({
                "success" : -1,
                "msg" : msg,
            }), 403
        return jsonify(
            {
                "success" : 1,
                "msg" : f"le prompt {data.get('nom')} a ete cree avec success",
            }
        ), 201
    except Exception as e :
        print("Une erreur s'est produite dans la fonction create_prompt de la route prompt ==> \n", e)
        return jsonify({
                "success" : -1,
                "msg" : "Une erreur s'est produite , veuillez reesayer",
        }), 500
    
    