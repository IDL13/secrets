from .models import *

from fastapi import FastAPI
from .handlers import Handlers

class App():
    
    def new(handlers = Handlers("secrets")):
        app = FastAPI()
        
        @app.get("/")
        async def helth():
            return handlers.helth()
        
        @app.post("/generate")
        async def generate(request: GenerateRequest):
            return handlers.generate(request)
        
        @app.post("/secret/{secret_key}")
        async def secret(secret_key: str, request: SecretRequest):
            return handlers.secret(secret_key, request)
    
        return app 
    
