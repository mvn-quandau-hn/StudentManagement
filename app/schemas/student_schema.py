from typing import Optional
from pydantic import BaseModel,Extra

class StudentBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    dob: str
    gender: str
    class Config:
        extra = Extra.forbid

class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    dob: Optional[str] = None
    gender: Optional[str] = None
