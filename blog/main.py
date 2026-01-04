from fastapi import FastAPI
from . import schemas, models
from .database import eng


app = FastAPI()

models.Base.metadata.create_all(eng)

@app.post('/blog')
def create(req: schemas.Blog):
    return req