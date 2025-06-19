from abc import ABC, abstractmethod
from typing import List, Optional
from app.model.grade import Grade

class IGradeRepository(ABC):

    @abstractmethod
    def create(self, grade: Grade) -> Grade:
        pass

    @abstractmethod
    def get_by_id(self, grade_id: int) -> Optional[Grade]:
        pass

    @abstractmethod
    def get_all(self) -> List[Grade]:
        pass

    @abstractmethod
    def update(self, grade: Grade, data: dict) -> Grade:
        pass

    @abstractmethod
    def delete(self, grade: Grade) -> None:
        pass