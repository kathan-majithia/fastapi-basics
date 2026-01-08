from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import eng,get_db
from sqlalchemy.orm import Session, joinedload
from typing import List
from .hashing import Hash
from .routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(eng)

app.include_router(authentication.router)

app.include_router(blog.router)

app.include_router(user.router)