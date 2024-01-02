from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session


from mypackage import crud, database

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/items")
async def items(request: Request, db: Session = Depends(database.get_db)):
    db_items = crud.get_items(db)
    return templates.TemplateResponse(request, "views/items.html", {"items": db_items})
