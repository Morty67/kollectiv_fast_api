from app.models import Task
from app.repositories.task_repository import TaskRepository
from app.serializers.task_serializer import (
    TaskResponse,
    TaskUpdate,
    TaskDelete,
)


class TaskService:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    async def get_all_tasks(self) -> list[TaskResponse]:
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
        return TaskResponse(
            id=task.id,
            title=task.title,
            description=task.description,
            category_id=task.category_id,
            priority=task.priority,
            user_id=task.user_id,
        )

    async def get_task(self, task_id: int):
        return await self.task_repo.get_task_by_id(task_id)

    async def update_task(self, task_id: int, task_update: TaskUpdate):
        existing_task = await self.task_repo.get_task_by_id(task_id)
        if not existing_task:
            return None  # Task not found, return None

        # Update the task data and return the updated task
        updated_task = await self.task_repo.update_task(task_id, task_update)
        return updated_task

    async def delete_task(self, task_id: int) -> TaskDelete:
        return await self.task_repo.delete_task(task_id)
