from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .views import router


def get_app() -> FastAPI:
    app = FastAPI(redoc_url=None)
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(router)
    return app
