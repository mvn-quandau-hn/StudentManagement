from pydantic import BaseModel, Field, validator
from typing import Optional

class GradeBase(BaseModel):
    student_id: int
    subject_id: int
    score: float

    @validator('score')
    def score_must_be_in_range(cls, v):
        if not 0 <= v <= 10:
            raise ValueError("Score must be between 0 and 10")
        return v

class GradeCreate(GradeBase):
    pass

class GradeRead(GradeBase):
    id: int

class GradeUpdate(BaseModel):
    score: float

    @validator('score')
    def score_must_be_in_range(cls, v):
        if not 0 <= v <= 10:
            raise ValueError("Score must be between 0 and 10")
        return v
