from app.database import async_session
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy.future import select
from app.crud import create_task, get_task
from app import schemas
from app import crud

router = APIRouter()


async def get_db():
    db = async_session()
    try:
        yield db
    finally:
        await db.close()


# @router.get('/hello')
# async def hello():
#     return "hello"
# stmt = select(Account)
# result = await db.execute(stmt)
# return result

# @router.get('/hello')
# async def hello(db: AsyncSession = Depends(get_db)):
#     stmt = select(Task)
#     result = await db.execute(stmt)
#     # print(result.all()[0])
#     return result.all()[0]


@router.post('/task', response_model=schemas.Task)
async def create_task(task: schemas.TaskCreate, db: AsyncSession = Depends(get_db)):
    db_task = await crud.create_task(db, task=task)
    return db_task


@router.get('/task', response_model=schemas.Task)
async def _get_task(taskdate: schemas.TaskDate, db: AsyncSession = Depends(get_db)):
    result = await crud.get_task(db, task_date=taskdate)
    return result
