from pydantic import BaseModel
from datetime import date

class HabitCreate(BaseModel):
    name: str
    description: str | None = None

class HabitOut(BaseModel):
    id: int
    name: str
    description: str
    user_id: int
    created_at: date

    class Config:
        from_attributes = True
