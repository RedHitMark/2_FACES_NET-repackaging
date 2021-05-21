from fastapi import APIRouter

from . import healthcheck_router
from . import upload_router
from . import validation_router
from . import download_router
from . import hack_router
from . import entries_router


router = APIRouter()


router.include_router(healthcheck_router.router, prefix='/healthcheck', tags=['health-check'])
router.include_router(upload_router.router, prefix='/upload', tags=['upload'])
router.include_router(validation_router.router, prefix='/validation', tags=['validation'])
router.include_router(download_router.router, prefix='/download', tags=['download'])
router.include_router(hack_router.router, prefix='/hack', tags=['hack'])
router.include_router(entries_router.router, prefix='/entries', tags=['entries'])
