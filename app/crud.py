from sqlalchemy.ext.asyncio import AsyncSession
from app import schemas, models
from sqlalchemy import select
import datetime


async def create_task(db: AsyncSession, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


async def get_task(db: AsyncSession, task_date: schemas.TaskDate):
    stmt = select(models.Task).where(models.Task.work_date >= task_date.begin_date).where(
        models.Task.work_date <= task_date.end_date)
    result = await db.execute(stmt)
    return result
