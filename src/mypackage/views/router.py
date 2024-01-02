from fastapi import APIRouter

from mypackage.views.endpoints import home, users, items

views_router = APIRouter()

views_router.include_router(home.router)
views_router.include_router(users.router)
views_router.include_router(items.router)
