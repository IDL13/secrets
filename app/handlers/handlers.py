import models
import hashlib
import os

from fastapi.encoders import jsonable_encoder
from databases.mongodb import MongoDB
from dotenv import load_dotenv
from crypto import MD5

load_dotenv()

class Handlers:
    def __init__(self, collection_name: str):
        self.mongo_db = MongoDB(os.getenv("MONGO_DB_URL"), collection_name)
    
    def helth(self):
        return {"message": "[SERVER STARTED]"}
    
    def generate(self, request: models.GenerateRequest):
        request_data = jsonable_encoder(request)
        
        secret_key = hashlib.sha256(request_data["secret"].encode()).hexdigest()

        passphrase = MD5(request_data["passphrase"]).encrypt()
        
        json = {
            "secret": request_data["secret"],
            "passphrase": passphrase,
            "secret_key": secret_key
        }

        try:
            _ = self.mongo_db.add_secret(json)
            
            return models.GenerateResponse(secret_key=secret_key).model_dump()
        
        except:
            bad_request = "Bad Request (Check your request)"
            
            return models.GenerateResponse(secret_key=bad_request).model_dump()
    
    def secret(self, secret_key: str, request: models.SecretRequest):
        request_data = jsonable_encoder(request)

        passphrase = MD5(request_data["passphrase"]).encrypt()
        
        json = {
            "secret_key": secret_key,
            "passphrase": passphrase
        }
        
        try:
            secret = self.mongo_db.get_secret(json)
            
            return models.SecretsResponse(secret=secret).model_dump()
        
        except:
            bad_request = "Bad Request (Secret_key & passhprase not found)"
            
            return models.GenerateResponse(secret_key=bad_request).model_dump()
