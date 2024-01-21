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
    model = Task

    async def get_all_tasks(self) -> List[TaskResponse]:
        tasks = await self.get_all()
        return [TaskResponse(
            id=task.id,
            title=task.title,
            description=task.description,
            category_id=task.category_id,
            priority=task.priority,
            user_id=task.user_id,
        ) for task in tasks]

    async def create_task(
            self,
            title: str,
            description: str,
            category_id: int,
            priority: str,
            user_id: int,
    ):
        return await self.create(
            title=title,
            description=description,
            category_id=category_id,
            priority=priority,
            user_id=user_id,
        )

    async def get_task_by_id(self, task_id: int):
        query = select(self.model).where(self.model.id == task_id)
        return await self.get_one(query)

    async def update_task(
            self, task_id: int, task_update: TaskUpdate
    ) -> Optional[Task]:
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
        task = await self.get_task_by_id(task_id)
        if task:
            await self.delete(task_id)
            return TaskDelete(deleted=True,
                              message="Task deleted successfully")
        return TaskDelete(deleted=False, message="Task not found")
