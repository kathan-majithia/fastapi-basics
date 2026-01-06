from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import eng,get_db
from sqlalchemy.orm import Session, joinedload
from typing import List
from .hashing import Hash
from .routers import blog

app = FastAPI()

models.Base.metadata.create_all(eng)

app.include_router(blog.router)

@app.post('/user',tags=['Users'])
def create(req: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=req.name,email=req.email,password=Hash.bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
@app.get('/user/{id}',response_model=schemas.ShowUser,tags=['Users'])
def display(id: int ,db: Session = Depends(get_db)):
    user = db.query(models.User).options(joinedload(models.User.blogs)).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user