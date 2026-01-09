from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import schemas, models
from .database import eng,get_db
from sqlalchemy.orm import Session, joinedload
from typing import List
from .hashing import Hash
from .routers import blog, user, authentication
import os

# For frontend
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8181"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# @app.get("/")
# def index():
#     return FileResponse("frontend/index.html")

# @app.get("/{page_name}")
# def serve_pages(page_name: str):
#     file_path = f"frontend/{page_name}.html"
#     if not os.path.exists(file_path):
#         raise HTTPException(status_code=404)
#     return FileResponse(file_path)



# app.mount('/static', StaticFiles(directory="frontend"),name="static")

models.Base.metadata.create_all(eng)

app.include_router(authentication.router, prefix="/api")

app.include_router(blog.router, prefix="/api")

app.include_router(user.router, prefix="/api")