from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.url import URLCreate, URLUpdate
from app.db import crud

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "URL Shortener"})

@router.get("/manage/", response_class=HTMLResponse)
def read_manage(request: Request):
    return templates.TemplateResponse("manage.html", {"request": request, "title": "Manage URLs"})

@router.post("/shorten/")
def shorten_url(url_create: URLCreate, db: Session = Depends(get_db)):
    short_url = crud.create_url(db, url_create)
    return {"shortened_url": short_url}

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


