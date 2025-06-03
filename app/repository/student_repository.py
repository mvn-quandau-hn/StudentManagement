from abc import ABC, abstractmethod
from typing import List, Optional
from app.model.student import Student

class IStudentRepository(ABC):

    @abstractmethod
    def create(self, student: Student) -> Student:
        pass

    @abstractmethod
    def get_by_id(self, student_id: int) -> Optional[Student]:
        pass

    @abstractmethod
    def get_all(self) -> List[Student]:
        pass

    @abstractmethod
    def update(self, student: Student, data: dict) -> Student:
        pass

    @abstractmethod
    def delete(self, student: Student) -> None:
        pass