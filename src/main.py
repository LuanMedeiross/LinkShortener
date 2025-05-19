from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from pydantic import BaseModel
from src.database.db import get_db

app = FastAPI()
db = get_db()
links = db["links"]

class URLParamsModel(BaseModel):
    url: str = None
    url_id: str = None

@app.post(f"/shorten/")
def shorten(model: URLParamsModel, request: Request):

    domain = request.headers.get("host", "")
    
    if not model.url or not model.url_id:
        return JSONResponse(
            content = {'message': 'Missing params'}, 
            status_code = 404
        )
    
    links.insert_one({
        "url": model.url,
        "url_id": model.url_id,
        "redirects": 0
    })

    return JSONResponse(
        content = {"link": f"{domain}/{model.url_id}"},
        status_code = 201
    )


