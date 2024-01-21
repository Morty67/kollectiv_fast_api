from typing import List, Optional

from sqlalchemy import select, update

from app.models import Task
from app.repositories.base_repository import BaseRepository
from app.serializers.task_serializer import (
    TaskResponse,
    TaskUpdate,
    TaskDelete,
)


class TaskRepository(BaseRepository):
    """
    TaskRepository extends BaseRepository and provides specific methods,
        for interacting with the 'Task' model.

    Attributes:
        model (Task): The SQLAlchemy model associated with the repository.

    Methods:
        - async def get_all_tasks(self) -> List[TaskResponse]:
    """

    model = Task

    async def get_all_tasks(self) -> List[TaskResponse]:
        """
        Fetches all tasks from the database and returns them as a list
            of TaskResponse objects.

        Returns:
            List[TaskResponse]: List of TaskResponse objects representing,
                the tasks.
        """
        tasks = await self.get_all()
        return [
            TaskResponse(
                id=task.id,
                title=task.title,
                description=task.description,
                category_id=task.category_id,
                priority=task.priority,
                user_id=task.user_id,
            )
            for task in tasks
        ]

    async def create_task(
        self,
        title: str,
        description: str,
        category_id: int,
        priority: str,
        user_id: int,
    ) -> TaskResponse:
        """
        Creates a new task with the provided information.

        Args:
            title (str): Title of the task.
            description (str): Description of the task.
            category_id (int): ID of the category to which the task belongs.
            priority (str): Priority level of the task.
            user_id (int): ID of the user associated with the task.

        Returns:
            TaskResponse: The created task information wrapped in a response
                object.
        """
        return await self.create(
            title=title,
            description=description,
            category_id=category_id,
            priority=priority,
            user_id=user_id,
        )

    async def get_task_by_id(self, task_id: int) -> Optional[TaskResponse]:
        """
        Retrieves a task by its ID and returns it as a TaskResponse object.

        Args:
            task_id (int): ID of the task to retrieve.

        Returns:
            TaskResponse: The task information wrapped in a response object.
            None: If the task is not found.
        """
        query = select(self.model).where(self.model.id == task_id)
        return await self.get_one(query)

    async def update_task(
        self, task_id: int, task_update: TaskUpdate
    ) -> Optional[Task]:
        """
        Updates the task data based on the provided ID and update information.

        Args:
            task_id (int): ID of the task to update.
            task_update (TaskUpdate): Data to update the task.

        Returns:
            TaskResponse: The updated task information wrapped in a response
                object.
            None: If the task is not found.
        """
        query = (
            update(self.model)
            .where(self.model.id == task_id)
            .values(task_update.dict())
        )
        await self.session.execute(query)
        await self.session.commit()

        # Get the updated task and return it
        updated_task = await self.get_task_by_id(task_id)
        return updated_task

    async def delete_task(self, task_id: int) -> TaskDelete:
        """
        Deletes a task based on the provided ID.

        Args:
            task_id (int): ID of the task to delete.

        Returns:
            TaskDelete: A response object indicating the success or failure,
                of the deletion.
        """
        task = await self.get_task_by_id(task_id)
        if task:
            await self.delete(task_id)
            return TaskDelete(
                deleted=True, message="Task deleted successfully"
            )
        return TaskDelete(deleted=False, message="Task not found")
