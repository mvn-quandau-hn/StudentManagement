from sqlmodel import SQLModel, create_engine,Session
from sqlalchemy.orm import sessionmaker

sqlite_url = "sqlite:///StudentManagement.db"
engine = create_engine(sqlite_url, echo=True)
SessionLocal = sessionmaker(bind=engine)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session