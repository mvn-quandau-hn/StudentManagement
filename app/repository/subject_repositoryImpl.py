from sqlmodel import Session, select
from typing import List, Optional
from app.model.subject import Subject
from app.repository.subject_repository import ISubjectRepository

class SubjectRepository(ISubjectRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, subject: Subject) -> Subject:
        self.session.add(subject)
        self.session.commit()
        self.session.refresh(subject)
        return subject

    def get_by_id(self, subject_id: int) -> Optional[Subject]:
        return self.session.get(Subject, subject_id)

    def get_all(self) -> List[Subject]:
        return self.session.exec(select(Subject)).all()

    def update(self, subject: Subject, data: dict) -> Subject:
        for key, value in data.items():
            setattr(subject, key, value)
        self.session.commit()
        self.session.refresh(subject)
        return subject

    def delete(self, subject: Subject) -> None:
        self.session.delete(subject)
        self.session.commit()