from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db


def get_all(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

def create(req: schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title,body=req.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return req

def show_id(id: int,res: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    return blog

def delete_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {"data":"deleted"}

def update_blog(id: int,req: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.update({'title':req.title,'body':req.body})
    db.commit()
    return {"data":"updated"}