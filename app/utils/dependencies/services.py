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
    repo = UserRepository(session)
    service = UserService(user_repo=repo)

    return service


def get_task_service(
    session: AsyncSession = Depends(get_session),
) -> TaskService:
    repo = TaskRepository(session)
    service = TaskService(task_repo=repo)
    return service


def get_category_service(
    session: AsyncSession = Depends(get_session),
) -> CategoryService:
    repo = CategoryRepository(session)
    service = CategoryService(
        category_repo=repo,
    )
    return service
