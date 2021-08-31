from fastapi import APIRouter
from api.api_v1_0 import api_v_1_0_router

router = APIRouter(prefix='/api')
router.include_router(api_v_1_0_router)
