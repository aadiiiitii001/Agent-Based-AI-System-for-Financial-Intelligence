from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://task_management_db_jbl0_user:udergQYDYSwFaHHIA1gXYbmKZPWywuwA@dpg-d53vh08gjchc73fh2to0-a/task_management_db_jbl0"  # replace with PostgreSQL later

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
