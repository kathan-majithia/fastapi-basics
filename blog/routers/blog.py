from typing import List
from fastapi import APIRouter, Depends, status, Response, HTTPException
from .. import schemas, models
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)

@router.get('/',response_model=List[schemas.ShowBlog])
def all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(req: schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title,body=req.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return req


@router.get('/{id}', status_code=200,response_model=schemas.ShowBlog)
def show(id: int,res: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
        # res.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} is not available'}
    return blog

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {"data":"deleted"}

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id: int,req: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.update({'title':req.title,'body':req.body})
    db.commit()
    return {"data":"updated"}