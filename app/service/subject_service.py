from typing import List
from app.schemas.subject_schema import SubjectCreate, SubjectUpdate
from app.model.subject import Subject
from app.repository.subject_repository import ISubjectRepository
from app.exceptions import APIException

class SubjectService:
    def __init__(self, repo: ISubjectRepository):
        self.repo = repo

    def create_subject(self, data: SubjectCreate) -> Subject:
        subject = Subject.from_orm(data)
        return self.repo.create(subject)

    def get_subject(self, subject_id: int) -> Subject:
        subject = self.repo.get_by_id(subject_id)
        if not subject:
            raise APIException(status_code=404, message="Subject not found")
        return subject

    def list_subjects(self) -> List[Subject]:
        return self.repo.get_all()

    def update_subject(self, subject_id: int, data: SubjectUpdate) -> Subject:
        subject = self.get_subject(subject_id)
        if not subject:
            raise APIException(status_code=404, message="Subject not found")
        update_data = data.dict(exclude_unset=True)
        return self.repo.update(subject, update_data)

    def delete_subject(self, subject_id: int) -> None:
        subject = self.get_subject(subject_id)
        if not subject:
            raise APIException(status_code=404, message="Subject not found")
        self.repo.delete(subject)