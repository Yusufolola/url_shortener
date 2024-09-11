from sqlalchemy import Column, Integer, String
from app.db.base import Base

class URLModel(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    original_url = Column(String, nullable=False)
    shortened_url = Column(String, nullable=False)
