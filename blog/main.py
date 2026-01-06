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

# get_db = database.get_db

@app.post('/blog',status_code=status.HTTP_201_CREATED, tags=['Blogs'])
def create(req: schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(title=req.title,body=req.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return req

# @app.get('/blog',response_model=List[schemas.ShowBlog])
# @app.get('/blog', tags=['Blogs'])
# def all(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

@app.get('/blog/{id}', status_code=200,response_model=schemas.ShowBlog,tags=['Blogs'])
def show(id: int,res: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
        # res.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with the id {id} is not available'}
    return blog

@app.delete('/blog/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=['Blogs'])
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.delete(synchronize_session=False)
    db.commit()
    return {"data":"deleted"}

@app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED,tags=['Blogs'])
def update(id: int,req: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with the id {id} is not available')
    blog.update({'title':req.title,'body':req.body})
    db.commit()
    return {"data":"updated"}

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