from pydantic import BaseModel, Field
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str
    
    # class Config:
    #     orm_mode = True
        
        
class Blog(BlogBase):
    class Config():
        orm_mode = True        
class User(BaseModel):
    name: str
    email: str
    password: str
    blog: Optional[List] = None
    # user_id: int
    
    class Config:
        orm_mode = True
        
class ShowBlog(BlogBase):
    title: str
    creator: User
    user_id: Optional[int]
    class Config():
        orm_mode = True
        
class ShowUser(BaseModel):

    name: str
    email: str
    blogs: List[ShowBlog] = []
    user_id: int = Field(alias="id")
    
    class Config():
        orm_mode = True
        allow_population_by_field_name = True