from flask import Blueprint, jsonify
from app.auth.authorization.decorators import superuser_required
from app.lib import db

from flask_jwt_extended import jwt_required

analytics_bp = Blueprint("analytics", __name__)


@analytics_bp.route("/")
# @jwt_required()   
# @superuser_required
def get_analitics():
    sum_transactions = db.get_sum_transactions().get("sum")
    total_users = db.get_table_count("users")
    total_prompts = db.get_table_count("prompts")
    total_goups = db.get_table_count("groups")
    recent_transactions = db.get_recent_transactions()
    users = db.get_data_table("users")[:10]
    response = {
        "success" : 1,
        "data" : {
        "transactions" : {
            "sum" : sum_transactions,
            "recent" : recent_transactions
            },
        "users" : {
            "total" : total_users,
            "data" : users
            },
        "prompts" : {
            "total" : total_prompts
            },
        "groups" : {
            "total" : total_goups
        }
        }
    }
    return jsonify(response), 200