# novo arquivo: create_db.py
from database import engine, Base
import models

Base.metadata.create_all(bind=engine)
