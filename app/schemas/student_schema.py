from typing import Optional
from pydantic import BaseModel, Field, validator
import re

class StudentBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    dob: str
    gender: str

class StudentCreate(BaseModel):
    name: str
    email: str
    phone: str
    address: str
    dob: str
    gender: str

    @validator('email')
    def email_must_be_gmail(cls, v):
        pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
        if not re.match(pattern, v):
            raise ValueError("Email must end with @gmail.com")
        return v

    @validator('phone')
    def phone_must_be_valid(cls, v):
        pattern = r'^0[0-9]{9}$'
        if not re.match(pattern, v):
            raise ValueError("Phone number must start with 0 and have exactly 10 digits")
        return v

    @validator('dob')
    def dob_must_be_valid(cls, v):
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, v):
            raise ValueError("Date of birth must be in the format YYYY-MM-DD")
        return v

    @validator('gender')
    def gender_must_be_valid(cls, v):
        allowed = {'male', 'female'}
        if v.lower() not in allowed:
            raise ValueError("Gender must be either 'male' or 'female'")
        return v.capitalize()


class StudentRead(StudentBase):
    id: int


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    dob: Optional[str] = None
    gender: Optional[str] = None

    @validator('email')
    def email_must_be_gmail(cls, v):
        if v is None:
            return v
        pattern = r'^[a-zA-Z0-9_.+-]+@gmail\.com$'
        if not re.match(pattern, v):
            raise ValueError("Email must end with @gmail.com")
        return v

    @validator('phone')
    def phone_must_be_valid(cls, v):
        if v is None:
            return v
        pattern = r'^0[0-9]{9}$'
        if not re.match(pattern, v):
            raise ValueError("Phone number must start with 0 and have exactly 10 digits")
        return v

    @validator('dob')
    def dob_must_be_valid(cls, v):
        if v is None:
            return v
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, v):
            raise ValueError("Date of birth must be in the format YYYY-MM-DD")
        return v

    @validator('gender')
    def gender_must_be_valid(cls, v):
        if v is None:
            return v
        allowed = {'male', 'female'}
        if v.lower() not in allowed:
            raise ValueError("Gender must be either 'male' or 'female'")
        return v.capitalize()
