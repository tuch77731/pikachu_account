from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession

db_user = "tch"
db_password = "1234qwer"
db_host = "192.168.50.201"
db_port = "15432"
db_name = "pikachu_account"

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, echo=True
)
async_session = sessionmaker(bind=engine,
                             autocommit=False,
                             autoflush=False,
                             expire_on_commit=False,
                             class_=AsyncSession)

Base = declarative_base()
