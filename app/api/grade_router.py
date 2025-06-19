from fastapi import APIRouter, Depends
from typing import List
from app.schemas.grade_schema import GradeCreate, GradeRead, GradeUpdate
from app.db.database import get_session
from sqlmodel import Session
from app.repository.grade_repositoryImpl import GradeRepository
from app.service.grade_service import GradeService

router = APIRouter(prefix="/grades", tags=["Grades"])

def get_service(session: Session = Depends(get_session)) -> GradeService:
    repo = GradeRepository(session)
    service = GradeService(repo)
    return service

@router.post("/", response_model=GradeRead)
def create_grade(grade: GradeCreate, service: GradeService = Depends(get_service)):
    return service.create_grade(grade)

@router.get("/", response_model=List[GradeRead])
def list_grades(service: GradeService = Depends(get_service)):
    return service.list_grades()

@router.get("/{grade_id}", response_model=GradeRead)
def get_grade(grade_id: int, service: GradeService = Depends(get_service)):
    return service.get_grade(grade_id)

@router.put("/{grade_id}", response_model=GradeRead)
def update_grade(grade_id: int, grade: GradeUpdate, service: GradeService = Depends(get_service)):
    return service.update_grade(grade_id, grade)

@router.delete("/{grade_id}")
def delete_grade(grade_id: int, service: GradeService = Depends(get_service)):
    service.delete_grade(grade_id)
    return {"success": True, "error": "", "data": None}
