from fastapi import APIRouter, Depends
from typing import List
from app.schemas.subject_schema import SubjectCreate, SubjectRead, SubjectUpdate
from app.db.database import get_session
from sqlmodel import Session
from app.repository.subject_repositoryImpl import SubjectRepository
from app.service.subject_service import SubjectService

router = APIRouter(prefix="/subjects", tags=["Subjects"])

def get_service(session: Session = Depends(get_session)) -> SubjectService:
    repo = SubjectRepository(session)
    return SubjectService(repo)

@router.post("/", response_model=SubjectRead)
def create_subject(subject: SubjectCreate, service: SubjectService = Depends(get_service)):
    return service.create_subject(subject)

@router.get("/", response_model=List[SubjectRead])
def list_subjects(service: SubjectService = Depends(get_service)):
    return service.list_subjects()

@router.get("/{subject_id}", response_model=SubjectRead)
def get_subject(subject_id: int, service: SubjectService = Depends(get_service)):
    return service.get_subject(subject_id)

@router.put("/{subject_id}", response_model=SubjectRead)
def update_subject(subject_id: int, subject: SubjectUpdate, service: SubjectService = Depends(get_service)):
    return service.update_subject(subject_id, subject)

@router.delete("/{subject_id}")
def delete_subject(subject_id: int, service: SubjectService = Depends(get_service)):
    service.delete_subject(subject_id)
    return {"success": True, "error": "", "data": None}
