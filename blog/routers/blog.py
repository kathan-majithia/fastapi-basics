from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from ..database import get_db
from ..repository import blog


router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    return blog.get_all(db)

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(req: schemas.Blog,db: Session = Depends(get_db)):
    return blog.create(req,db)


@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog)
def show(id: int,res: Response, db: Session = Depends(get_db)):
    return blog.show_id(id,res,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    
    return blog.delete_blog(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id: int,req: schemas.Blog, db: Session = Depends(get_db)):
    
    return blog.update_blog(id,req,db)