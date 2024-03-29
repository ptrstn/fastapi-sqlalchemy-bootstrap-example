from typing import List

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from mypackage import crud, schemas, database

router = APIRouter(tags=["items"])


@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items


@router.get("/items/{item_id}", response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(database.get_db)):
    item = crud.get_item(db, item_id)
    return item


@router.post(
    "/items/", response_model=schemas.Item, status_code=status.HTTP_201_CREATED
)
def create_item(item: schemas.ItemCreate, db: Session = Depends(database.get_db)):
    db_item = crud.create_item(db, item)
    return db_item


@router.post(
    "/users/{user_id}/items/",
    response_model=schemas.Item,
    status_code=status.HTTP_201_CREATED,
)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(database.get_db)
):
    try:
        db_item = crud.create_item_for_user(db, user_id, item)
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id '{user_id}' not found",
        )
    return db_item


@router.delete("/items/{item_id}")
async def delete_api_item(item_id: int, db: Session = Depends(database.get_db)):
    try:
        crud.delete_item(db=db, item_id=item_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}
