from typing import Optional
import datetime
from pydantic import BaseModel


class TaskBase(BaseModel):
    firm: str
    amount: int
    location: str
    work: str
    work_date: datetime.date
    deal: bool
    deal_date: datetime.date
    remark: str


class TaskCreate(TaskBase):
    class Config:
        orm_mode = True


class Task(TaskBase):
    pass


class TaskDate(BaseModel):
    begin_date: datetime.date
    end_date: datetime.date