from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session, joinedload
from ..database import get_db
from ..hashing import Hash

def create_user(req: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=req.name,email=req.email,password=Hash.bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
def display_users(id: int ,db: Session = Depends(get_db)):
    user = db.query(models.User).options(joinedload(models.User.blogs)).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user


def display_all(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return users