from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from mypackage import crud, database

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/users")
async def users(request: Request, db: Session = Depends(database.get_db)):
    db_users = crud.get_users(db)
    return templates.TemplateResponse(request, "views/users.html", {"users": db_users})
