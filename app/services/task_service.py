from app.models import Task
from app.repositories.task_repository import TaskRepository
from app.serializers.task_serializer import (
    TaskResponse,
    TaskUpdate,
    TaskDelete,
)


class TaskService:
    """
    Service class for handling task-related operations.

    This class provides methods for interacting with tasks, including
    creating, retrieving, updating, and deleting tasks.

    Attributes:
        task_repo (TaskRepository): The repository for handling task data.
    """

    def __init__(self, task_repo: TaskRepository):
        """
        Initialize the TaskService with a TaskRepository instance.

        Args:
            task_repo (TaskRepository): The repository for handling task data.
        """
        self.task_repo = task_repo

    async def get_all_tasks(self) -> list[TaskResponse]:
        """
        Get a list of all tasks.

        Returns:
            List[TaskResponse]: The list of tasks.
        """
        tasks = await self.task_repo.get_all_tasks()
        return tasks

    async def create_task(
        self,
        title: str,
        description: str,
        category_id: int,
        priority: str,
        user_id: int,
    ) -> TaskResponse:
        """
        Create a new task.

        Args:
            title (str): The title of the task.
            description (str): The description of the task.
            category_id (int): The ID of the category to which the task belongs.
            priority (str): The priority of the task.
            user_id (int): The ID of the user associated with the task.

        Returns:
            TaskResponse: The response containing the created task information.
        """
        task_data = {
            "title": title,
            "description": description,
            "category_id": category_id,
            "priority": priority,
            "user_id": user_id,
        }
        task = await self.task_repo.create_task(**task_data)
        return self._create_task_response(task)

    def _create_task_response(self, task: Task) -> TaskResponse:
        """
        Create a TaskResponse object from a Task instance.

        Args:
            task (Task): The task instance.

        Returns:
            TaskResponse: The response containing task information.
        """
        return TaskResponse(
            id=task.id,
            title=task.title,
            description=task.description,
            category_id=task.category_id,
            priority=task.priority,
            user_id=task.user_id,
        )

    async def get_task(self, task_id: int):
        """
        Get task information by ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            TaskResponse: The response containing the task information.
        """
        return await self.task_repo.get_task_by_id(task_id)

    async def update_task(self, task_id: int, task_update: TaskUpdate):
        """
        Update an existing task.

        Args:
            task_id (int): The ID of the task to update.
            task_update (TaskUpdate): The data for updating the task.

        Returns:
            None: If the task with the given ID doesn't exist.
            Any: The result of the update operation.
        """
        existing_task = await self.task_repo.get_task_by_id(task_id)
        if not existing_task:
            return None  # Task not found, return None

        # Update the task data and return the updated task
        updated_task = await self.task_repo.update_task(task_id, task_update)
        return updated_task

    async def delete_task(self, task_id: int) -> TaskDelete:
        """
        Delete a task by ID.

        Args:
            task_id (int): The ID of the task to delete.

        Returns:
            TaskDelete: The response containing the result of the delete
                operation.
        """
        return await self.task_repo.delete_task(task_id)
