from pydantic import BaseModel
from typing import Optional, List

class BloggerBase(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    password: str

class CreateBlogger(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class BloggerInfo(BaseModel):
    bloggerDB:List[BloggerBase]

class Response(BaseModel):
    message: Optional[str] = None
    data: Optional[BloggerBase | BloggerInfo] = None
    