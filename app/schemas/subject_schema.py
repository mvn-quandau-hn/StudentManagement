from typing import Optional
from pydantic import BaseModel, validator
import re

class SubjectBase(BaseModel):
    name: str

class SubjectCreate(SubjectBase):
    @validator('name')
    def name_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("Subject name must not be blank")
        return v

class SubjectRead(SubjectBase):
    id: int

class SubjectUpdate(BaseModel):
    name: str

    @validator('name')
    def name_must_not_be_blank(cls, v):
        if v is not None and not v.strip():
            raise ValueError("Subject name must not be blank")
        return v
