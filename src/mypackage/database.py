from pydantic_settings import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, declarative_base


class Settings(BaseSettings):
    DB_DIALECT: str = "sqlite"
    DB_FILE: str = "database.db"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str = "mydatabase"
    DB_USER: str = "myuser"
    DB_PASSWORD: str = "mypassword"


settings = Settings()

if settings.DB_DIALECT == "sqlite":
    SQLALCHEMY_DATABASE_URL = f"{settings.DB_DIALECT}:///{settings.DB_FILE}"
    # https://fastapi.tiangolo.com/tutorial/sql-databases/#note
    engine = create_engine(
        url=SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
else:
    SQLALCHEMY_DATABASE_URL = (
        f"{settings.DB_DIALECT}"
        f"://"
        f"{settings.DB_USER}"
        f":"
        f"{settings.DB_PASSWORD}"
        f"@"
        f"{settings.DB_HOST}"
        f":"
        f"{settings.DB_PORT}"
        f"/"
        f"{settings.DB_NAME}"
    )
    engine = create_engine(
        url=SQLALCHEMY_DATABASE_URL,
    )


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeBase = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)


def get_db():
    with SessionLocal() as db:
        yield db
