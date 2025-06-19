from typing import List
from app.schemas.grade_schema import GradeCreate, GradeUpdate
from app.model.grade import Grade
from app.repository.grade_repository import IGradeRepository
from app.exceptions import APIException
from app.db.database import SessionLocal
from app.generate_faiss import generate_faiss_index

class GradeService:
    def __init__(self, repo: IGradeRepository):
        self.repo = repo

    def create_grade(self, grade_data: GradeCreate) -> Grade:
        grade = Grade.from_orm(grade_data)
        new_grade = self.repo.create(grade)
        generate_faiss_index()
        return new_grade

    def get_grade(self, grade_id: int) -> Grade:
        grade = self.repo.get_by_id(grade_id)
        if not grade:
            raise APIException(status_code=404, message="Grade not found")
        return grade

    def list_grades(self) -> List[Grade]:
        return self.repo.get_all()

    def update_grade(self, grade_id: int, update_data: GradeUpdate) -> Grade:
        grade = self.get_grade(grade_id)
        update_dict = update_data.dict(exclude_unset=True)
        updated_grade = self.repo.update(grade, update_dict)
        generate_faiss_index()
        return updated_grade

    def delete_grade(self, grade_id: int) -> None:
        grade = self.get_grade(grade_id)
        self.repo.delete(grade)
        generate_faiss_index()
