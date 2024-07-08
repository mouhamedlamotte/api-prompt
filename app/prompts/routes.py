import base64
import hashlib
import bcrypt

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.auth.authorization.decorators import staff_required
from app.lib import db



prompt_bp = Blueprint("prompt", __name__)
@prompt_bp.route("/",methods=["GET"])
@jwt_required()
def get_prompt(): 
    if request.method == 'OPTIONS':
        return '', 204
    res = db.get_data_table("prompts")
    return jsonify(res), 200
    


@prompt_bp.route("/new", methods=["POST"])
@jwt_required()
def create_prompt():
    try :
        data =  request.get_json()
        usermail = get_jwt_identity()
        user = db.get_user_by_email(usermail)
        if not user :
            return ({"success" : -1, "msg" : "Unauthorized"}), 401
        if  user.get("is_superuser"):
            return ({"success" : -1,"msg" : "Vous ne pouvez pas creer de prompt en tant que admin"}), 401
        if not data.get("title") and not data.get("text"):
            return jsonify({"success" : -1, "msg" : "veuillez fournir le titre(title) et le contenu (text) du prompt "}), 403
        data["created_by"] = user.get("uid")
        res = db.create_prompt(**data)
        if res[0] == False:
            return jsonify({
                "success" : -1,
                "msg" : res[1]
            })
        return jsonify({
                "success" : 1,
                "msg" : "Le prompt a ete cree avec success"
            }), 200
    except Exception as e:
        # Gestion des erreurs
        print(f"Erreur lors de la récupération des données: {e}")
        return jsonify({"message": "Une erreur s'est produite lors de la récupération des données."}), 500
    
    
@prompt_bp.route("/votes/new", methods=["POST"])
@jwt_required()
def create_vote():
    try :
        data =  request.get_json()
        u_email = get_jwt_identity()
        user = db.get_user_by_email(u_email)
        if user and user.get("is_superuser"):
            return ({"success" : -1, "msg" : "Unauthorized"}), 401
        if not  data.get("prompt_id"):
            return jsonify({
                "success" : -1,
                "msg" : "Prompt (prompt_id) id required"
            }), 403
        check_if_prompt_exist = db.get_prompt_by_id(data.get("prompt_id"))
        if not check_if_prompt_exist :
            return jsonify({
                "success" : -1,
                "msg" : "Prompt does not exist"
            }), 403
        if user.get("uid") == check_if_prompt_exist.get("created_by"):
            return jsonify({
                "success" : -1,
                "msg" : "You cannot vote on your own prompt"
            }), 403
        check_if_user_already_voted = db.get_vote_by_uid_and_pid(user.get("uid"), data.get("prompt_id"))
        if check_if_user_already_voted:
            return jsonify({
                "success" : -1,
                "msg" : "User already voted"
            }), 403
        data["uid"] = user.get("uid")
        vote_value = 1
        prompt_created_by_group_id = db.get_group_member_by_uid(check_if_prompt_exist.get("created_by"))
        print(prompt_created_by_group_id)
        voting_user_group_id = db.get_group_member_by_uid(user.get("uid"))
        print(voting_user_group_id)
        if prompt_created_by_group_id.get("group_id") == voting_user_group_id.get("group_id"):
            vote_value = 2
        else :
            vote_value = 1
        print(prompt_created_by_group_id.get("group_id") == voting_user_group_id.get("group_id"))
        data["value"] = vote_value
        res = db.add_vote(**data)
        votes = db.get_sum_votes_by_pid(data.get("prompt_id"))
        print(votes.get("sum"))
        if votes.get("sum") >= 6 : db.update_prompt_state(data.get("prompt_id"),"active")
        if res[0] == False:
            return jsonify({
                "success" : -1,
                "msg" : res[1]
            })
        return jsonify({
                "success" : 1,
                "msg" : "Le vote a ete cree avec success"
            }), 200
    except Exception as e:
        print(f"Erreur lors de la création des données: {e}")
        return jsonify({"message": "Une erreur s'est produite lors de la création des données."}), 500
    
@prompt_bp.route("/notes/new", methods=["POST"])
@jwt_required()
def create_note():
    try:
        data =  request.get_json()
        u_email = get_jwt_identity()
        user = db.get_user_by_email(u_email)
        if user and user.get("is_superuser"):
            return ({"success" : -1, "msg" : "Unauthorized"}), 401
        if not  data.get("prompt_id") and not data.get("value"):
            return jsonify({
                "success" : -1,
                "msg" : "Prompt id (prompt_id) and vote_value (value) are required"
            }), 403
        if data.get("value") < -10 or data.get("value") > 10 :
            return jsonify({
                "success" : -1,
                "mgs" : "Note value must be between -10 and +10"
            }), 403
        check_if_prompt_exist = db.get_prompt_by_id(data.get("prompt_id"))
        if not check_if_prompt_exist :
            return jsonify({
                "success" : -1,
                "msg" : "Prompt does not exist"
            }), 403
        if user.get("uid") == check_if_prompt_exist.get("created_by"):
            return jsonify({
                "success" : -1,
                "msg" : "You cannot note on your own prompt"
            }), 403
        check_if_user_already_notes = db.get_notes_by_uid_and_pid(user.get("uid"), data.get("prompt_id"))
        if check_if_user_already_notes:
            return jsonify({
                "success" : -1,
                "msg" : "User already note"
            }), 403
        data["uid"] = user.get("uid")
        vote_value_percent = 1
        prompt_created_by_group_id = db.get_group_member_by_uid(check_if_prompt_exist.get("created_by"))
        voting_user_group_id = db.get_group_member_by_uid(user.get("uid"))
        if prompt_created_by_group_id.get("group_id") == voting_user_group_id.get("group_id"):
            vote_value_percent = data.get("value") * 0.4
        else :
            vote_value_percent = data.get("value") * 0.6
        data["value"] = vote_value_percent
        res = db.add_note(**data)
        notes_avg = db.get_avg_notes_by_pid(data.get("prompt_id")).get("avg")
        print(notes_avg)
        new_price = 1000 * (1 + notes_avg)
        db.update_prompt_price(data.get("prompt_id"), new_price)
        if res[0] == False:
            return jsonify({
                "success" : -1,
                "msg" : res[1]
            })
        return jsonify({
                "success" : 1,
                "msg" : "La note a ete cree avec success"
            }), 201
    except Exception as e :
        print(f"Erreur lors de la création des données: {e}")
        return jsonify({"message": "Une erreur s'est produite lors de la création des données."}), 500