from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session, joinedload
from ..database import get_db
from ..hashing import Hash
from ..repository import user
router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/')
def create(req: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(req,db)
    
@router.get('/',response_model=List[schemas.ShowUser])
def all(db: Session = Depends(get_db)):
    return user.display_all(db)


@router.get('/{id}',response_model=schemas.ShowUser)
def display(id: int ,db: Session = Depends(get_db)):
    return user.display_users(id,db)


