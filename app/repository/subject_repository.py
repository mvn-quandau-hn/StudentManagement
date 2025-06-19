from abc import ABC, abstractmethod
from typing import List, Optional
from app.model.subject import Subject

class ISubjectRepository(ABC):
    @abstractmethod
    def create(self, subject: Subject) -> Subject: pass

    @abstractmethod
    def get_by_id(self, subject_id: int) -> Optional[Subject]: pass

    @abstractmethod
    def get_all(self) -> List[Subject]: pass

    @abstractmethod
    def update(self, subject: Subject, data: dict) -> Subject: pass

    @abstractmethod
    def delete(self, subject: Subject) -> None: pass