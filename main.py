from src.app import App
import uvicorn
from fastapi import FastAPI

app = App.new()
        
if __name__ == "__main__":
    uvicorn.run(app,
        host="0.0.0.0",
        port=8000,
        reload=True,
        access_log=False
    )
