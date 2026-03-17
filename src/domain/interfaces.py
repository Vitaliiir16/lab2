from abc import ABC, abstractmethod
from src.domain.models import CsvEnrollmentRow, Student, Course, Enrollment

class IFileReader(ABC):
    @abstractmethod
    def read(self, path: str) -> list[CsvEnrollmentRow]:
        raise NotImplementedError

class IStudentRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Student | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, student: Student) -> Student:
        raise NotImplementedError

class ICourseRepository(ABC):
    @abstractmethod
    def get_by_code(self, code: str) -> Course | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, course: Course) -> Course:
        raise NotImplementedError

class IEnrollmentRepository(ABC):
    @abstractmethod
    def get_by_student_and_course(self, student_id: int, course_id: int) -> Enrollment | None:
        raise NotImplementedError

    @abstractmethod
    def save(self, enrollment: Enrollment) -> Enrollment:
        raise NotImplementedError

class IUnitOfWork(ABC):
    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError
