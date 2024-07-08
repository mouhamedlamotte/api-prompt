from flask import Blueprint, jsonify, request
from app.lib import db,send_mail, paytech

transaction_bp = Blueprint("transaction", __name__)

@transaction_bp.route("/buy_prompt", methods=["POST"])
def buy_prompt():
    data = request.get_json()
    print(request.headers.get("Authorization"))
    if request.headers.get("Authorization"):
        return jsonify({
            "success": -1,
            "msg": "Only visitor can buy prompt"
        })
    if not data.get("prompt_id") or not isinstance(data.get("prompt_id"), int):
        return jsonify({
            "success": -1,
            "msg": "prompt_id is required"
        }), 400
    prompt_id = data.get("prompt_id")
    prompt = db.get_prompt_by_id(prompt_id)
    if not prompt:
        return jsonify({
            "success": -1,
            "msg": "prompt does not exist"
        }), 400
    if prompt.get("state") != "active":
        return jsonify({
            "success": -1,
            "msg": "prompt is not available"
        })
    if not data.get("buyer_info") or not isinstance(data.get("buyer_info"), dict):
        return jsonify({
            "success": -1,
            "msg": "buyer_info (mail at least) in dict is required"
        })
    if not data.get("buyer_info").get("email"):
        return jsonify({
            "success": -1,
            "msg": "mail is required"
        })
    buyer_info = data.get("buyer_info")
    price = prompt.get("price")
    
    res = db.add_transaction(buyer_info, prompt_id, price)
    if res == False :
        return jsonify({
            "success": -1,
            "msg": "Une erreur s'est produite , veuillez reesayer"
        }), 400
    buyer_name = buyer_info.get("name")
    send_mail({
        "to": buyer_info.get("email"),
        "subject": "Transaction effectue avec success",
        "html": f"""
        <div>
        <h3>
            Merci pour votre confiance {buyer_name if buyer_name else ""},
        <h4>
            PROMPT : {prompt.get("title")}
        </h4>
        <p>
            {prompt.get("text")}
        </p>
        </div>
        """
    })
    return jsonify({
        "success": 1,
        "msg": "Transaction effectue avec success"
    }), 201
    
    
    
@transaction_bp.route("/test_paytech", methods=["GET"])
def test_paytech():
    res, data = paytech.create_payment({
    "item_name" : "Prompt 1",
    "item_price" : 1000,
    })
    if res == False :
        return jsonify({
            "success": -1,
            "msg": "Une erreur s'est produite , veuillez reesayer"
        })
    return data