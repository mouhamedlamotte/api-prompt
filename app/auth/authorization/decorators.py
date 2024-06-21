import functools
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.lib import db


def staff_required(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        email = get_jwt_identity()
        user = db.get_user_by_email(email)
        print(user)
        if user and user.get("is_staff"):
            return func(*args, **kwargs)
        return jsonify({
            "success": -1,
            "msg": "Unauthorized"}), 401
    return decorated

def superuser_required(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        email = get_jwt_identity()
        user = db.get_user_by_email(email)
        if user and user.get("is_superuser"):
            return f(*args, **kwargs)
        return jsonify({
            "success": -1,
            "msg": "Unauthorized"}), 401
    return decorated