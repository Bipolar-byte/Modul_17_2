from fastapi import FastAPI
from app.models.task import Task
from app.models.user import User
from routers.user import router as user_router
from routers.task import router as task_router
from sqlalchemy.schema import CreateTable
from app.backend.db import engine

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user_router)
app.include_router(task_router)

if __name__ == "__main__":
    print(CreateTable(User.__table__).compile(engine))
    print(CreateTable(Task.__table__).compile(engine))