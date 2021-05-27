from app.database import Base
from sqlalchemy import Column, DateTime, Integer, String, Boolean, TEXT, text, Date


class Task(Base):
    __tablename__ = "task"
    uid = Column(Integer, primary_key=True)
    firm = Column(String)
    amount = Column(Integer)
    location = Column(String)
    work = Column(String)
    work_date = Column(Date, index=True)
    deal = Column(Boolean, index=True)
    deal_date = Column(Date)
    remark = Column(TEXT)
    insert_time = Column(DateTime, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
    delete = Column(Boolean)
