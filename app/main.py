from fastapi import FastAPI
from app.router.task import router
from app.database import Base, engine

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    print('hello')

    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


app.include_router(router, prefix="/hello")
