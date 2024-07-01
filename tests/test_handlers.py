import hashlib

from src.handlers import Handlers
from src.models import *

handlers = Handlers("tests")

def test_helth():
    
    # then
    assert handlers.helth() == {
        "message": "[SERVER STARTED]"
    }
    
def test_generate():
    # given
    secret_key = hashlib.sha256("test".encode()).hexdigest()
    
    request = GenerateRequest(
        secret="test",
        passphrase="test"
    )
    
    # then
    assert handlers.generate(request) == GenerateResponse(
        secret_key=secret_key
    ).model_dump()
    
def test_secret():
    # given
    secret_key = hashlib.sha256("test".encode()).hexdigest()
    
    request = SecretRequest(
        passphrase="test"
    )
    
    # then
    assert handlers.secret(secret_key, request) == SecretsResponse(
        secret="test"
    ).model_dump()