from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models, oauth2
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/',response_model=List[schemas.ShowBlog])
def display_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create_new_blog(req: schemas.Blog,db: Session = Depends(get_db)):
    return blog.create(req,db)


@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog)
def display_specific_blog(id: int,res: Response, db: Session = Depends(get_db)):
    return blog.show_id(id,res,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    
    return blog.delete_blog(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int,req: schemas.Blog, db: Session = Depends(get_db)):
    
    return blog.update_blog(id,req,db)