from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.habit import Habit
from app.schemas import habit as habit_schema
from app.models.user import User
from app.utils.getUser import get_current_user

router = APIRouter(prefix="/habits", tags=["Habits"])

@router.post("/", response_model=habit_schema.HabitOut)
def create_habit(
    habit: habit_schema.HabitCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_habit = Habit(**habit.dict(), user_id=current_user.id)
    db.add(new_habit)
    db.commit()
    db.refresh(new_habit)
    return new_habit

@router.get("/", response_model=list[habit_schema.HabitOut])
def list_habits(db: Session = Depends(get_db), user_id: int = 1):
    return db.query(Habit).filter(Habit.user_id == user_id).all()