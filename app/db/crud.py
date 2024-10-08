from sqlalchemy.orm import Session
from app.models.url import URLModel  # Use SQLAlchemy model
from app.schemas.url import URLCreate, URLUpdate  # Use Pydantic schemas for validation
from app.logic.url_shortening import generate_short_url


def create_url(db: Session, url_create: URLCreate) -> str:
    # Check if the original URL already exists in the database
    existing_url = db.query(URLModel).filter(URLModel.original_url == str(url_create.original_url)).first()
    
    # If the URL exists, return the existing shortened URL
    if existing_url:
        return existing_url.shortened_url

    # If the URL does not exist, generate a new shortened URL
    short_url = generate_short_url(url_create.length)
    db_url = URLModel(
        original_url=str(url_create.original_url),  # Convert Url to string
        shortened_url=short_url
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url.shortened_url
    
def update_url(db: Session, short_url: str, url_update: URLUpdate) -> str:
    db_url = db.query(URLModel).filter(URLModel.shortened_url == short_url).first()  # Use URLModel
    if db_url is None:
        return None
    
    if url_update.original_url:
        db_url.original_url = url_update.original_url
    if url_update.length:
        db_url.shortened_url = generate_short_url(url_update.length)  # Update shortened_url
    
    db.commit()
    db.refresh(db_url)
    return db_url.shortened_url

def delete_url(db: Session, short_url: str) -> None:
    db_url = db.query(URLModel).filter(URLModel.shortened_url == short_url).first()  # Use URLModel
    if db_url:
        db.delete(db_url)
        db.commit()
