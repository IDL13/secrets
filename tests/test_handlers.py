import models
import hashlib

from app.handlers import Handlers

handlers = Handlers("tests")

def test_helth():
    
    # then
    assert handlers.helth() == {
        "message": "[SERVER STARTED]"
    }
    
def test_generate():
    # given
    secret_key = hashlib.sha256("test".encode()).hexdigest()
    
    request = models.GenerateRequest(
        secret="test",
        passphrase="test"
    )
    
    # then
    assert handlers.generate(request) == models.GenerateResponse(
        secret_key=secret_key
    ).model_dump()
    
def test_secret():
    # given
    secret_key = hashlib.sha256("test".encode()).hexdigest()
    
    request = models.SecretRequest(
        passphrase="test"
    )
    
    # then
    assert handlers.secret(secret_key, request) == models.SecretsResponse(
        secret="test"
    ).model_dump()