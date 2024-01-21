from typing import Any, List

from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select


class BaseRepository:
    """
    BaseRepository provides common CRUD operations for SQLAlchemy models,
        with asynchronous support.

    Attributes:
        model (Any): The SQLAlchemy model associated with the repository.
        session (AsyncSession): The asynchronous database session, used for
            operations.
    """

    model: Any = None

    def __init__(self, session: AsyncSession):
        """
        Initializes the BaseRepository instance with a database session.

        Args:
            session (AsyncSession): The asynchronous database session,
                used for operations.
        """
        self.session = session

    async def get_all(self) -> List:
        """
        Fetch all instances of the associated model from the database.

        Returns:
            List: A list of instances of the associated model.
        """
        query = Select(self.model)
        response = await self.session.execute(query)
        return response.scalars().all()

    async def create(self, **kwargs) -> Any:
        """
        Create a new instance of the model with the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments representing the fields of the model.

        Returns:
            Any: The created instance of the model.
        """
        instance = self.model(**kwargs)
        self.session.add(instance)
        await self.session.commit()
        return instance

    async def exists(self, query: Select) -> bool:
        """
        Checks if instance exists in the database based on the provided query.

        Args:
            query (Select): The SQLAlchemy query object.

        Returns:
            bool: True if an instance exists, False otherwise.
        """
        query = query.with_only_columns(self.model.id)
        response = await self.session.execute(query)

        result = response.first()
        return bool(result)

    async def get_one(self, query: Select) -> Any:
        """
        Fetch a single instance from the database based on the provided query.

        Args:
            query (Select): The SQLAlchemy query object.

        Returns:
            Any: The fetched instance or None if not found.
        """
        response = await self.session.execute(query)
        result = response.scalars().first()
        return result

    async def delete(self, obj_id: int) -> None:
        """
        Deletes an instance from the database using its ID.

        Args:
            obj_id (int): The ID of the instance to be deleted.
        """
        query = delete(self.model).where(self.model.id == obj_id)
        await self.session.execute(query)
        await self.session.commit()

    async def save(self, obj: Any) -> None:
        """
        Adds and commits an instance to the database session.

        Args:
            obj (Any): The instance to be saved.
        """
        self.session.add(obj)
        await self.session.commit()
