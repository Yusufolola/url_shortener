from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

class URLBase(BaseModel):
    original_url: HttpUrl

class URLCreate(URLBase):
    length: Optional[int] = Field(6, ge=4, le=12, description="Length of the shortened URL")

class URLUpdate(BaseModel):
    original_url: Optional[HttpUrl] = None
    length: Optional[int] = Field(6, ge=4, le=12, description="New length of the shortened URL")

class URL(URLBase):
    id: int
    shortened_url: Optional[str]

    class Config:
        orm_mode = True
