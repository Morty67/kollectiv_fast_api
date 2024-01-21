from fastapi import APIRouter, Depends, HTTPException

from app.auth.security import get_current_active_profile
from app.models import User
from app.serializers.task_serializer import (
    TaskResponse,
    TaskCreate,
    TaskList,
    TaskUpdate,
    TaskDelete,
)
from app.services.task_service import TaskService
from app.utils.dependencies.services import get_task_service

router = APIRouter()


@router.post("/create_task/", response_model=TaskResponse)
async def create_task(
    item: TaskCreate,
    current_user: User = Depends(get_current_active_profile),
    service: TaskService = Depends(get_task_service),
):
    return await service.create_task(**item.dict(), user_id=current_user.id)


@router.get("/all_tasks/", response_model=TaskList)
async def get_all_tasks(
    service: TaskService = Depends(get_task_service),
):
    tasks = await service.get_all_tasks()
    return TaskList(tasks=tasks)


@router.get("/tasks/{tasks_id}", response_model=TaskResponse)
async def read_task_by_id(
    task_id: int, service: TaskService = Depends(get_task_service)
):
    task = await service.get_task(task_id)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task_by_id(
    task_id: int,
    task_update: TaskUpdate,
    service: TaskService = Depends(get_task_service),
):
    task = await service.update_task(task_id, task_update)
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/tasks/{task_id}", response_model=TaskDelete)
async def delete_task_by_id(
    task_id: int, service: TaskService = Depends(get_task_service)
):
    deleted_task = await service.delete_task(task_id)
    if deleted_task:
        return deleted_task
    raise HTTPException(status_code=404, detail="Task not found")
