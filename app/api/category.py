from fastapi import APIRouter, Depends, HTTPException

from app.serializers.category_serializer import (
    CategoryCreate,
    CategoryResponse,
    CategoryList,
    CategoryUpdate,
    CategoryDelete,
)
from app.services.category_service import CategoryService
from app.utils.dependencies.services import get_category_service

router = APIRouter()


@router.get("/all_categories/", response_model=CategoryList)
async def get_all_categories(
    service: CategoryService = Depends(get_category_service),
):
    return await service.get_all_categories()


@router.post("/create-category/", response_model=CategoryResponse)
async def create_category(
    category_create: CategoryCreate,
    service: CategoryService = Depends(get_category_service),
):
    return await service.create_category(category_create)


@router.get("/categories/{category_id}", response_model=CategoryResponse)
async def read_category_by_id(
    category_id: int, service: CategoryService = Depends(get_category_service)
):
    category = await service.get_category(category_id)
    if category:
        return category
    raise HTTPException(status_code=404, detail="Category not found")


@router.put("/categories/{category_id}", response_model=CategoryResponse)
async def update_category_by_id(
    category_id: int,
    category_update: CategoryUpdate,
    service: CategoryService = Depends(get_category_service),
):
    category = await service.update_category(category_id, category_update)
    if category:
        return category
    raise HTTPException(status_code=404, detail="Category not found")


@router.delete("/categories/{category_id}", response_model=CategoryDelete)
async def delete_category_by_id(
    category_id: int, service: CategoryService = Depends(get_category_service)
):
    deleted_category = await service.delete_category(category_id)
    if deleted_category:
        return deleted_category
    raise HTTPException(status_code=404, detail="Category not found")
