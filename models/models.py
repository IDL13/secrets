from pydantic import BaseModel

class GenerateRequest(BaseModel):
    secret: str
    passphrase: str

class GenerateResponse(BaseModel):
    secret_key: str

class SecretRequest(BaseModel):
    passphrase: str
    
class SecretsResponse(BaseModel):
    secret: str