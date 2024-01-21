from app.repositories.category_repository import CategoryRepository
from app.serializers.category_serializer import (
    CategoryCreate,
    CategoryList,
    CategoryUpdate,
    CategoryDelete,
    CategoryResponse,
)


class CategoryService:
    def __init__(self, category_repo: CategoryRepository):
        self.category_repo = category_repo

    async def create_category(
        self, category_create: CategoryCreate
    ) -> CategoryResponse:
        category = await self.category_repo.create_category(
            category_create.dict()
        )
        return CategoryResponse(id=category.id, name=category.name)

    async def category_exists(self, category_id: int):
        return await self.category_repo.category_exists(category_id)

    async def get_category(self, category_id: int):
        return await self.category_repo.get_category_by_id(category_id)

    async def get_all_categories(self) -> CategoryList:
        categories = await self.category_repo.get_all_categories()
        return CategoryList(
            categories=[
                CategoryResponse(id=cat.id, name=cat.name)
                for cat in categories
            ]
        )

    async def update_category(
        self, category_id: int, category_update: CategoryUpdate
    ):
        # Перевіряємо, чи існує категорія за вказаним ідентифікатором
        existing_category = await self.category_repo.get_category_by_id(
            category_id
        )
        if not existing_category:
            return None  # Категорія не знайдена, повертаємо None

        # Оновлюємо категорію та повертаємо результат
        return await self.category_repo.update_category(
            category_id, category_update
        )

    async def delete_category(self, category_id: int) -> CategoryDelete:
        return await self.category_repo.delete_category(category_id)
