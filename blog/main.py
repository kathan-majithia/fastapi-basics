from fastapi import FastAPI, Depends
from . import schemas, models
from .database import eng,SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(eng)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/blog')
def create(req: schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title,body=req.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return req