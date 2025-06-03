from typing import List, Optional
from sqlmodel import Session, select
from app.model.student import Student
from app.repository.student_repository import IStudentRepository

class StudentRepository(IStudentRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, student: Student) -> Student:
        self.session.add(student)
        self.session.commit()
        self.session.refresh(student)
        return student

    def get_by_id(self, student_id: int) -> Optional[Student]:
        return self.session.get(Student, student_id)

    def get_all(self) -> List[Student]:
        return self.session.exec(select(Student)).all()

    def update(self, student: Student, data: dict) -> Student:
        for key, value in data.items():
            setattr(student, key, value)
        self.session.commit()
        self.session.refresh(student)
        return student

    def delete(self, student: Student) -> None:
        self.session.delete(student)
        self.session.commit()
