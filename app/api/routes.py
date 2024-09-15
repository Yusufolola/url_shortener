from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.url import URLCreate, URLUpdate
from app.db import crud
from app.models.url import URLModel

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "URL Shortener"})

@router.get("/manage/", response_class=HTMLResponse)
def read_manage(request: Request):
    return templates.TemplateResponse("crud.html", {"request": request, "title": "Manage URLs"})

@router.post("/shorten/")
def shorten_url(url_create: URLCreate, db: Session = Depends(get_db)):
    short_url = crud.create_url(db, url_create)
    full_shortened_url = f"https://url-shortener-4-2owt.onrender.com/{short_url}"
    return {"shortened_url": full_shortened_url}

@router.get("/{shortened_path}")
def redirect_to_url(shortened_path: str, db: Session = Depends(get_db)):
    # Look up the original URL associated with the shortened path
    db_url = db.query(URLModel).filter(URLModel.shortened_url == shortened_path).first()
    
    if db_url:
        # Redirect to the original URL
        return RedirectResponse(url=db_url.original_url)
    else:
        # If the shortened URL does not exist, raise a 404 error
        raise HTTPException(status_code=404, detail="Shortened URL not found")

@router.put("/{short_url}")
def update_url(short_url: str, url_update: URLUpdate, db: Session = Depends(get_db)):
    updated_url = crud.update_url(db, short_url, url_update)
    if updated_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"updated_url": updated_url}

@router.delete("/{short_url}")
def delete_url(short_url: str, db: Session = Depends(get_db)):
    crud.delete_url(db, short_url)
    return {"detail": "URL deleted successfully"}


