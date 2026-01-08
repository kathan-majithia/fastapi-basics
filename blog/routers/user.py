from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, oauth2
from sqlalchemy.orm import Session, joinedload
from ..database import get_db
from ..hashing import Hash
from ..repository import user
router = APIRouter(
    prefix="/user",
    tags=['Users']
)

@router.post('/')
def create_new_user(req: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(req,db)
    
@router.get('/',response_model=List[schemas.ShowUser])
def display_all_users(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.display_all(db)


@router.get('/{id}',response_model=schemas.ShowUser)
def display_specific_user(id: int ,db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.display_users(id,db)


