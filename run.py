import uvicorn

from src.main import app

uvicorn.run(app, host="localhost", port=8000)
