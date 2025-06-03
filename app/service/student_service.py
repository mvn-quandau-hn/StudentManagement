from typing import List
from app.schemas.student_schema import StudentCreate, StudentUpdate
from app.model.student import Student
from app.repository.student_repository import IStudentRepository
from app.exceptions import APIException

class StudentService:
    def __init__(self, repo: IStudentRepository):
        self.repo = repo

    def create_student(self, student_data: StudentCreate) -> Student:
        student = Student.from_orm(student_data)
        return self.repo.create(student)

    def get_student(self, student_id: int) -> Student:
        student = self.repo.get_by_id(student_id)
        if not student:
            raise APIException(status_code=404, message="Student not found")
        return student

    def list_students(self) -> List[Student]:
        return self.repo.get_all()

    def update_student(self, student_id: int, update_data: StudentUpdate) -> Student:
        student = self.get_student(student_id)
        if not student:
            raise APIException(status_code=404, message="Student not found")
        update_dict = update_data.dict(exclude_unset=True)
        return self.repo.update(student, update_dict)

    def delete_student(self, student_id: int) -> None:
        student = self.get_student(student_id)
        if not student:
            raise APIException(status_code=404, message="Student not found")
        self.repo.delete(student)
