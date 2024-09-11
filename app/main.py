from fastapi import FastAPI
from app.api import routes
from app.configuration.config import settings
from fastapi.staticfiles import StaticFiles
from app.db.session import init_db


app = FastAPI(title="URL Shortener")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(routes.router)

@app.on_event("startup")
def on_startup():
    init_db()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=settings.PORT)

