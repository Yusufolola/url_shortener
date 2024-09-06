from pydantic import BaseModel, HttpUrl, Field
from typing import Optional

class URLCreate(BaseModel):
    original_url: HttpUrl
    length: Optional[int] = Field(6, ge=4, le=12, description="Length of the shortened URL")
    
class URLUpdate(BaseModel):
    original_url: Optional[HttpUrl] = None
    length: Optional[int] = Field(6, ge=4, le=12, description="New length of the shortened URL")

