from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

@app.get("/")
def index():
    return {"data":"Hello"}

@app.get('/about')
def about():
    return {"name":"Kathan Majithia"}

@app.get('/blob')
def blob(limit=10,lod : bool = True,sort: Optional[str] = None):
    if lod:
        return {"data" : f"{limit} blobs from the db"}
    else:
        return {"data":"Not loaded"}

@app.get('/blob/{id}')
def show(id: int):
    return {"data":id}

class Blob(BaseModel):
    title: str
    body: str
    published: Optional[bool]
    

@app.post('/blob')
def create(req: Blob):
    return {'data':f"Blob is created with title as {req.title}"}

