from app.repositories.category_repository import CategoryRepository
from app.serializers.category_serializer import (
    CategoryCreate,
    CategoryList,
    CategoryUpdate,
    CategoryDelete,
    CategoryResponse,
)


class CategoryService:
    """
    CategoryService provides business logic for handling categories.

    Attributes:
        category_repo (CategoryRepository): The repository for category-related
            database operations.
    """

    def __init__(self, category_repo: CategoryRepository):
        """
        Initialize the CategoryService with a CategoryRepository instance.

        Args:
            category_repo (CategoryRepository): The repository for handling,
                category data.
        """
        self.category_repo = category_repo

    async def create_category(
        self, category_create: CategoryCreate
    ) -> CategoryResponse:
        """
        Create a new category.

        Args:
            category_create (CategoryCreate): The data for creating
                a new category.

        Returns:
            CategoryResponse: The response containing the created category
                information.
        """
        category = await self.category_repo.create_category(
            category_create.dict()
        )
        return CategoryResponse(id=category.id, name=category.name)

    async def category_exists(self, category_id: int):
        """
        Check if a category with the given ID exists.

        Args:
            category_id (int): The ID of the category to check.

        Returns:
            bool: True if the category exists, False otherwise.
        """
        return await self.category_repo.category_exists(category_id)

    async def get_category(self, category_id: int):
        """
        Get category information by ID.

        Args:
            category_id (int): The ID of the category to retrieve.

        Returns:
            CategoryResponse: The response containing the category information.
        """
        return await self.category_repo.get_category_by_id(category_id)

    async def get_all_categories(self) -> CategoryList:
        """
        Get a list of all categories.

        Returns:
            CategoryList: The list of categories.
        """
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
        """
        Update an existing category.

        Args:
            category_id (int): The ID of the category to update.
            category_update (CategoryUpdate): The data for updating,
                the category.

        Returns:
            None: If the category with the given ID doesn't exist.
            Any: The result of the update operation.
        """
        existing_category = await self.category_repo.get_category_by_id(
            category_id
        )
        if not existing_category:
            return None

        return await self.category_repo.update_category(
            category_id, category_update
        )

    async def delete_category(self, category_id: int) -> CategoryDelete:
        """
        Delete a category by ID.

        Args:
            category_id (int): The ID of the category to delete.

        Returns:
            CategoryDelete: The response containing the result of the
                delete operation.
        """
        return await self.category_repo.delete_category(category_id)
