from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = "sqlite:///./habits.db"  # Ou a URL do seu banco

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ✅ Esta função é essencial para o uso com Depends()
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
