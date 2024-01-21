from sqlalchemy import update
from sqlalchemy.sql import select

from app.models import Category
from app.repositories.base_repository import BaseRepository
from app.serializers.category_serializer import (
    CategoryUpdate,
    CategoryDelete,
    CategoryResponse,
)


class CategoryRepository(BaseRepository):
    model = Category

    async def create_category(self, category_create: dict) -> Category:
        return await self.create(**category_create)

    async def category_exists(self, category_id: int):
        query = select(Category).filter(Category.id == category_id)
        return await self.exists(query)

    async def get_category_by_id(self, category_id: int) -> CategoryResponse:
        query = select(self.model).where(self.model.id == category_id)
        result = await self.get_one(query)

        if result:
            return CategoryResponse(id=result.id, name=result.name)
        else:
            return None

    async def get_all_categories(self):
        return await self.get_all()

    async def update_category(
            self, category_id: int, category_update: CategoryUpdate
    ):
        # Get the category by id
        category = await self.get_category_by_id(category_id)

        if category:
            # Update category data by its id
            query = (
                update(self.model)
                .where(self.model.id == category_id)
                .values(category_update.dict())
            )
            await self.session.execute(query)
            await self.session.commit()

            # Returning the updated category
            return await self.get_category_by_id(category_id)

        return None

    async def delete_category(self, category_id: int) -> CategoryDelete:
        # Get the category by id
        category = await self.get_category_by_id(category_id)

        if category:
            # Delete the category using the base repository method
            await self.delete(category_id)
            return CategoryDelete(
                deleted=True, message="Category deleted successfully"
            )

        # Message that the category does not exist
        return CategoryDelete(deleted=False, message="Category not found")