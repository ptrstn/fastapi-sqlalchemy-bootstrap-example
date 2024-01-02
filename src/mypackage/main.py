from fastapi import FastAPI

from mypackage.api.v1.router import api_router
from mypackage.views.router import views_router
from mypackage.database import init_db

init_db()

app = FastAPI()

app.include_router(api_router)
app.include_router(views_router)
