import datetime

from sqlalchemy import update

from app.models import User
from app.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository):
    """
    UserRepository extends BaseRepository and provides specific methods, for
        interacting with the 'User' model.

    Attributes:
        model (User): The SQLAlchemy model associated with the repository.
    """

    model = User

    async def get_user_by_email(self, email: str):
        """
        Retrieves a user by their email address and returns the user instance.

        Args:
            email (str): Email address of the user to retrieve.

        Returns:
            Optional[User]: The user instance if found, otherwise None.
        """
        query = self.model.__table__.select().where(self.model.email == email)
        return await self.get_one(query)

    async def get_user_by_username(self, username: str):
        """
        Retrieves a user by their username and returns the user instance.

        Args:
            username (str): Username of the user to retrieve.

        Returns:
            Optional[User]: The user instance if found, otherwise None.
        """
        query = self.model.__table__.select().where(
            self.model.username == username
        )
        return await self.get_one(query)

    async def exists_by_username(self, username: str) -> bool:
        """
        Checks if a user with the specified username exists in the database.

        Args:
            username (str): Username to check.

        Returns:
            bool: True if the user exists, False otherwise.
        """

        query = self.model.__table__.select().where(
            self.model.username == username
        )
        return await self.exists(query)

    async def exists_by_email(self, email: str) -> bool:
        """
        Checks if a user with the specified email exists in the database.

        Args:
            email (str): Email to check.

        Returns:
            bool: True if the user exists, False otherwise.
        """
        query = self.model.__table__.select().where(self.model.email == email)
        return await self.exists(query)

    async def get_one(self, query):
        """
        Executes a general query and returns the first result.

        Args:
            query: SQLAlchemy query object.

        Returns:
            Optional[User]: The first result of the query if found,
                otherwise None.
        """
        response = await self.session.execute(query)
        result = response.first()
        return result

    async def get_last_login(self, user_id: int):
        """
        Retrieves the last login timestamp for a user by their ID.

        Args:
            user_id (int): ID of the user.

        Returns:
            Optional[datetime.datetime]: The last login timestamp if found,
                otherwise None.
        """
        query = self.model.__table__.select().where(self.model.id == user_id)
        query = query.with_only_columns(self.model.last_login)
        response = await self.session.execute(query)
        result = response.scalar()
        return result

    async def update_last_login(self, user: User):
        """
        Updates the last login timestamp for a user.

        Args:
            user (User): The user instance to update.
        """
        query = (
            update(self.model)
            .where(self.model.id == user.id)
            .values(last_login=datetime.datetime.utcnow())
        )
        await self.session.execute(query)
        await self.session.commit()

    async def get_user_by_id(self, user_id: int):
        """
        Retrieves a user by their ID and returns the user instance.

        Args:
            user_id (int): ID of the user to retrieve.

        Returns:
            Optional[User]: The user instance if found, otherwise None.
        """
        query = self.model.__table__.select().where(self.model.id == user_id)
        return await self.get_one(query)

    async def update_last_request(self, user: User):
        """
        Updates the last request timestamp for a user.

        Args:
            user (User): The user instance to update.
        """
        query = (
            update(self.model)
            .where(self.model.id == user.id)
            .values(last_request=datetime.datetime.utcnow())
        )
        await self.session.execute(query)
        await self.session.commit()

    async def get_last_request(self, user_id: int):
        """
        Retrieves the last request timestamp for a user by their ID.

        Args:
            user_id (int): ID of the user.

        Returns:
            Optional[datetime.datetime]: The last request timestamp if found,
                otherwise None.
        """
        query = self.model.__table__.select().where(self.model.id == user_id)
        query = query.with_only_columns(self.model.last_request)
        response = await self.session.execute(query)
        result = response.scalar()
        return result
