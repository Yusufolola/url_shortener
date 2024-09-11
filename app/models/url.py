from pydantic import BaseModel, AnyHttpUrl
from typing import Optional
class URLBase(BaseModel):
    original_url: AnyHttpUrl

class URLCreate(URLBase):
    length: int

class URLUpdate(BaseModel):
    original_url: AnyHttpUrl = None
    length: int = None

class URL(URLBase):
    id: int
    shortened_url: Optional [str]

    class Config:
        orm_mode = True
