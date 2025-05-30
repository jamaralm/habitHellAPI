from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.habits import router as habit_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(habit_router)