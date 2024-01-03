from fastapi import APIRouter, Depends, Form, HTTPException
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from mypackage import crud, database, schemas

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/items")
async def items(request: Request, db: Session = Depends(database.get_db)):
    db_items = crud.get_items(db)
    db_users = crud.get_users(db)
    return templates.TemplateResponse(
        request, "views/items.html", {"items": db_items, "users": db_users}
    )


@router.post("/submit-item")
async def submit_item(
    title: str = Form(...),
    description: str = Form(...),
    user_id: int = Form(...),
    db: Session = Depends(database.get_db),
):
    item_create = schemas.ItemCreate(title=title, description=description)
    try:
        crud.create_item_for_user(db=db, user_id=user_id, item=item_create)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="User not found")
    return RedirectResponse(url="/items", status_code=303)
