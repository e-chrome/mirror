from fastapi import APIRouter

from app.api.v1 import mirror

api_router = APIRouter()
api_router.include_router(mirror.router, tags=['mirror'])
