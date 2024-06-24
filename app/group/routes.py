from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required


from app.auth.authorization.decorators import superuser_required
from app.lib import db


group_bp = Blueprint("group", __name__)

@group_bp.route("/group", methods=["POST"])
@jwt_required()
@superuser_required
def create_group():
    data = request.get_json()
    if not data.get("name"):
        return jsonify({
            "success": -1,
            "msg": "name is required"
        }), 400
    email = get_jwt_identity()
    user = db.get_user_by_email(email)
    res = db.create_group(data.get("name"), user.get("id"))
    if res == False :
        return jsonify({
            "success": -1,
            "msg": "Une erreur s'est produite , veuillez reesayer"
        }), 400
    return jsonify({
        "success": 1,
        "msg": f"Le groupe {data.get('name')} a ete cree avec success"
    }), 201

@group_bp.route("/groups", methods=["GET"])
@jwt_required()
@superuser_required
def get_groups():
    groups = db.get_data_table("groups")
    if request.args.get("members") == "true" :
        data = []
        for group in groups :
            group_members = db.get_group_member_by_gid(group.get("group_id"))
            group["members"] = group_members
            data.append(group)
        return jsonify(data), 200
    return jsonify(groups), 200

@group_bp.route("/add-member", methods=["POST"])
@jwt_required()
@superuser_required
def add_member():
    data = request.get_json()
    print(data)
    if not data.get("uid") or not data.get("group_id"):
        return jsonify({
            "success" : -1,
            "msg" : "User id (uid) and group (group_id) id required"
        })
    check_if_user_exist = db.get_user_by_id(data.get("uid"))
    if not check_if_user_exist :
        return jsonify({
            "success" : -1,
            "msg" : "User does not exist"
        })
    
    check_if_group_exist = db.get_group_by_id(data.get("group_id"))
    if not check_if_group_exist :
        return jsonify({
            "success" : -1,
            "msg" : "Group does not exist"
        })
    check_if_user_already_in_a_group = db.get_group_member_by_uid(data.get("uid"))
    if check_if_user_already_in_a_group:
        return jsonify({
            "success" : -1,
            "mgs" : "This user is already in a group"
        })
    res = db.add_member(data.get("uid"), data.get("group_id"))
    
    if not res :
        return jsonify({
            "success" : -1,
            "mgs" : "Une erreur s'est produite"
        }), 500
    
    return jsonify({
        "success" : 1,
        "msg" : "User ajoute avec success"
    }), 201