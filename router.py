from schemas import STaskAdd, Task
from typing import Annotated
from fastapi import  Depends, APIRouter
from repository import TaskRepository
from schemas import STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def add_task(task: Annotated[STaskAdd, Depends()]) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_tasks() -> list[Task]:
    tasks = await TaskRepository.get_all()
    return tasks

