from fastapi import APIRouter, Depends
from typing import List
from app.schemas.student_schema import StudentCreate, StudentRead, StudentUpdate
from app.db.database import get_session
from sqlmodel import Session
from app.repository.student_repositoryImpl import StudentRepository
from app.service.student_service import StudentService

router = APIRouter(prefix="/students", tags=["Students"])

def get_service(session: Session = Depends(get_session)) -> StudentService:
    repo = StudentRepository(session)
    service = StudentService(repo)
    return service

@router.post("/", response_model=StudentRead)
def create(student: StudentCreate, service: StudentService = Depends(get_service)):
    return service.create_student(student)

@router.get("/", response_model=List[StudentRead])
def get_all(service: StudentService = Depends(get_service)):
    return service.list_students()

@router.get("/{student_id}", response_model=StudentRead)
def get_one(student_id: int, service: StudentService = Depends(get_service)):
    return service.get_student(student_id)

@router.put("/{student_id}", response_model=StudentRead)
def update(student_id: int, student: StudentUpdate, service: StudentService = Depends(get_service)):
    return service.update_student(student_id, student)

@router.delete("/{student_id}")
def delete(student_id: int, service: StudentService = Depends(get_service)):
    service.delete_student(student_id)
    return {"success": True, "error": "", "data": None}
