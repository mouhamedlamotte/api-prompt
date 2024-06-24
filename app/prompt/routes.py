import base64
import hashlib
import bcrypt

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.auth.authorization.decorators import staff_required
from app.lib import db



prompt_bp = Blueprint("prompt", __name__)
@prompt_bp.route("/prompt",methods=["GET"])
@jwt_required()
def get_prompt(): 
    prompt = db.get_data_table("prompt")
    print(prompt)
    return jsonify(prompt), 200


@prompt_bp.route("/prompt", methods=["POST"])
def create_prompt():
    try :
        data =  request.get_json()
        if not data.get("title") and not data.get("text") and not data.get("tags") and not data.get("price")and not data.get("state"):
            return jsonify({
                "success" : -1,
                "msg" : "veuillez fournir les informations ",
            }), 403
         # Vérification si des données ont été trouvées
        if data is None:
            return jsonify({"message": "Aucune donnée trouvée dans la table 'prompt'."}), 404
        
        # Affichage des données dans la console pour le débogage
        print(data)
        
        # Renvoi des données au format JSON
        return jsonify(data), 200
    except Exception as e:
        # Gestion des erreurs
        print(f"Erreur lors de la récupération des données: {e}")
        return jsonify({"message": "Une erreur s'est produite lors de la récupération des données."}), 500
    
    