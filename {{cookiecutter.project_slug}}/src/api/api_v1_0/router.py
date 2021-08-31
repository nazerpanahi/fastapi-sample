from fastapi import APIRouter
from api.api_v1_0.endpoints.debug import router as debug_router
from config import settings

router = APIRouter(prefix='/v1.0')

if settings.DEBUG:
    router.include_router(debug_router)
