from sqlmodel import SQLModel, Field
from typing import Optional

class Grade(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    student_id: int = Field(foreign_key="student.id")
    subject_id: int = Field(foreign_key="subject.id")
    score: float
