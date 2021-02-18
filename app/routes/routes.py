from fastapi import APIRouter

from . import healthcheck
from . import upload


router = APIRouter()

router.include_router(healthcheck.router, prefix='/healthcheck', tags=['health-check'])
router.include_router(upload.router, prefix='/upload', tags=['upload'])
