from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from mypackage import schemas, crud
from mypackage.database import get_db


router = APIRouter(tags=["users"])


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = crud.create_user(db, user)
    except IntegrityError:
        db.rollback()
        existing_user = crud.get_user_by_email(db=db, email=user.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Email already registered",
            )
        raise

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "id": db_user.id,
            "email": db_user.email,
            "is_active": db_user.is_active,
        },
    )
