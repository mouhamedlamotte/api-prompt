import uuid

import json

import requests

from constant import PAYTECH_ENV, PAYTECH_API_KEY, PAYTECH_SECRET_KEY,PAYTECH_API_URL

class Paytech():
    def __init__(self) -> None:
        self.ref_command = str(uuid.uuid4())
        self.ipn_url = "https://c592-41-82-64-150.ngrok-free.app/paiement/ipn"
        self.env = PAYTECH_ENV
        self.currency = "XOF"
        self.headers = {
            'Content-Type': 'application/json',
            'api_key': PAYTECH_API_KEY,
            'api_secret': PAYTECH_SECRET_KEY
            }
        self.base_url = PAYTECH_API_URL
  
        
    def create_payment(self, data: dict):
        try : 
            payload = json.dumps({
            "item_name": data.get("item_name", "Prompt 1"),
            "item_price": data.get("item_price", 1000),
            "currency": "XOF",
            "ref_command": self.ref_command,
            "command_name": data.get("command_name", "Achat de prompt"),
            "ipn_url": self.ipn_url,
            "env": "test"
            })


            response = requests.request("POST", self.base_url, headers=self.headers, data=payload)
            return True, response.text            
        except Exception as e:
            print(e)
            message = "Une erreur s'est produite lors de l'operation de paiement"
            return False, message
        
