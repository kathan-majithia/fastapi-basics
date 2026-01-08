from pydantic import BaseModel, Field
from typing import List, Optional

class BlogBase(BaseModel):
    title: str
    body: str
    
    # class Config:
    #     orm_mode = True
        
        
class UserBase(BaseModel):
    name: str
    email: str
    
    class Config:
        orm_mode = True
class Blog(BlogBase):
    class Config():
        orm_mode = True        
        
class ShowBlog(BlogBase):
    title: str
    # creator: User
    creator: Optional[UserBase]
    user_id: Optional[int]
    class Config():
        orm_mode = True
        
class ShowUser(UserBase):

    # name: str
    # email: str
    id: int = Field(alias="user_id")
    blogs: List[ShowBlog] = []
    user_id: int = Field(alias="id")
    
    class Config():
        orm_mode = True
        allow_population_by_field_name = True
class User(UserBase):
    # name: str
    # email: str
    password: str
    # blog: Optional[List] = None
    # user_id: int
    
    class Config:
        orm_mode = True
        
class Login(BaseModel):
    username: str
    password: str