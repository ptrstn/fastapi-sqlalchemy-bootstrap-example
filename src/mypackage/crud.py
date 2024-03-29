from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session
from mypackage import models, schemas


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_item(db: Session, item_id: int):
    return db.get(models.Item, item_id)


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user(db: Session, user_id: int):
    return db.get(models.User, user_id)


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_item_for_user(db: Session, user_id: int, item: schemas.ItemCreate):
    db_user = db.get(models.User, user_id)

    if not db_user:
        raise NoResultFound(f"User with id {user_id} found")

    db_item = models.Item(**item.model_dump(), owner=db_user)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def delete_item(db: Session, item_id: int):
    db_item = db.get(models.Item, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    else:
        raise NoResultFound(f"Item with id {item_id} not found")
