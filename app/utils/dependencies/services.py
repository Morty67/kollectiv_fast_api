from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.category_repository import CategoryRepository
from app.repositories.task_repository import TaskRepository
from app.repositories.user_repository import UserRepository
from app.services.category_service import CategoryService
from app.services.task_service import TaskService
from app.services.user_service import UserService
from app.utils.dependencies.get_session import get_session


def get_user_service(
    session: AsyncSession = Depends(get_session),
) -> UserService:
    """
    Dependency function to obtain a UserService instance with a given
        AsyncSession.

    Args:
        session (AsyncSession, optional): An optional AsyncSession dependency
            obtained from get_session. Defaults to Depends(get_session).

    Returns:
        UserService: An instance of the UserService with the provided
            AsyncSession.
    """
    repo = UserRepository(session)
    service = UserService(user_repo=repo)

    return service


def get_task_service(
    session: AsyncSession = Depends(get_session),
) -> TaskService:
    """
    Dependency function to obtain a TaskService instance with a given
        AsyncSession.

    Args:
        session (AsyncSession, optional): An optional AsyncSession dependency
            obtained from get_session. Defaults to Depends(get_session).

    Returns:
        TaskService: An instance of the TaskService with the provided
            AsyncSession.
    """
    repo = TaskRepository(session)
    service = TaskService(task_repo=repo)
    return service


def get_category_service(
    session: AsyncSession = Depends(get_session),
) -> CategoryService:
    """
    Dependency function to obtain a CategoryService instance with a given
        AsyncSession.

    Args:
        session (AsyncSession, optional): An optional AsyncSession dependency
            obtained from get_session. Defaults to Depends(get_session).

    Returns:
        CategoryService: An instance of the CategoryService with the provided
            AsyncSession.
    """
    repo = CategoryRepository(session)
    service = CategoryService(
        category_repo=repo,
    )
    return service
