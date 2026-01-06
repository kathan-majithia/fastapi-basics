from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str
    body: str
    
    class Config:
        orm_mode = True
        
class User(BaseModel):
    name: str
    email: str
    password: str
    # user_id: int
    
    class Config:
        orm_mode = True
        
class ShowUser(BaseModel):
    name: str
    email: str
    user_id: int = Field(alias="id")
    
    class Config():
        orm_mode = True
        allow_population_by_field_name = True
        
class ShowBlog(BaseModel):
    title: str
    creator: ShowUser
    class Config():
        orm_mode = True