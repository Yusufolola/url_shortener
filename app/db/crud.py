from sqlalchemy.orm import Session
from app.models.url import URL
from app.models.url import URLCreate, URLUpdate
from app.logic.url_shortening import generate_short_url

def create_url(db: Session, url_create: URLCreate) -> str:
    short_url = generate_short_url(url_create.length)
    db_url = URL(original_url=url_create.original_url, short_url=short_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url.short_url

def update_url(db: Session, short_url: str, url_update: URLUpdate) -> str:
    db_url = db.query(URL).filter(URL.short_url == short_url).first()
    if db_url is None:
        return None
    
    if url_update.original_url:
        db_url.original_url = url_update.original_url
    if url_update.length:
        db_url.short_url = generate_short_url(url_update.length)
    
    db.commit()
    db.refresh(db_url)
    return db_url.short_url

def delete_url(db: Session, short_url: str) -> None:
    db_url = db.query(URL).filter(URL.short_url == short_url).first()
    if db_url:
        db.delete(db_url)
        db.commit()

