from fastapi import FastAPI
from src.homework.api.application import router as application_router
from src.homework.api.user import router as user_router
from src.homework.api.orders import router as orders_router
from src.homework.db.engine import engine
from src.homework.db.models import Base


def create_app() -> FastAPI:
    Base.metadata.create_all(engine)
    app = FastAPI()
    app.include_router(application_router, tags=["Create Applications"])
    app.include_router(user_router, tags=["Get Balance"])
    app.include_router(orders_router, tags=["Modify Orders"])
    return app
