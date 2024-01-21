from fastapi import APIRouter

from app.api.category import router as category_router
from app.api.images import router as image_router
from app.api.task import router as task_router
from app.api.user import router as user_router

api_router = APIRouter()

api_router.include_router(image_router, prefix='/images', tags=['Images'])
api_router.include_router(user_router, prefix="/users", tags=["User"])
api_router.include_router(
    category_router, prefix="/categories", tags=["Category"]
)
api_router.include_router(task_router, prefix="/tasks", tags=["Task"])
