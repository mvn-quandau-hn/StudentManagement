from typing import List, Optional
from sqlmodel import Session, select
from app.model.grade import Grade
from app.repository.grade_repository import IGradeRepository

class GradeRepository(IGradeRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, grade: Grade) -> Grade:
        self.session.add(grade)
        self.session.commit()
        self.session.refresh(grade)
        return grade

    def get_by_id(self, grade_id: int) -> Optional[Grade]:
        return self.session.get(Grade, grade_id)

    def get_all(self) -> List[Grade]:
        return self.session.exec(select(Grade)).all()

    def update(self, grade: Grade, data: dict) -> Grade:
        for key, value in data.items():
            setattr(grade, key, value)
        self.session.commit()
        self.session.refresh(grade)
        return grade

    def delete(self, grade: Grade) -> None:
        self.session.delete(grade)
        self.session.commit()