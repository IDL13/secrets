import hashlib

from fastapi import FastAPI
from fastapi.testclient import TestClient
from src.handlers import Handlers
from src.app import App

client = TestClient(App.new(handlers=Handlers("tests")))

def test_helth():
    # given
    response = client.get("/")
    
    # then
    assert response.status_code == 200
    assert response.json() == {"message": "[SERVER STARTED]"}
    
def test_generate():
    # given
    response = client.post(
        "/generate",
        json={
            "secret": "test",
            "passphrase": "test"
        }
    )
    
    secret_key_true = hashlib.sha256("test".encode()).hexdigest()
    
    assert response.status_code == 200
    assert response.json() == {
        "secret_key": secret_key_true
    }

def test_secret():
    # given
    secret_key = hashlib.sha256("test".encode()).hexdigest()
    response = client.post(
        "/secret/" + secret_key,
        json = {
            "passphrase": "test"
        }
    )
    
    # then
    assert response.status_code == 200
    assert response.json() == {
        "secret": "test"
    }
    
    
    