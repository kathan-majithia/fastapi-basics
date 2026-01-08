from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session, joinedload
from ..database import get_db
from ..hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/')
def create(req: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=req.name,email=req.email,password=Hash.bcrypt(req.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
@router.get('/{id}',response_model=schemas.ShowUser)
def display(id: int ,db: Session = Depends(get_db)):
    user = db.query(models.User).options(joinedload(models.User.blogs)).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user