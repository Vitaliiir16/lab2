from dataclasses import dataclass
from datetime import date

@dataclass
class CsvEnrollmentRow:
    student_email: str
    student_full_name: str
    group_name: str
    course_code: str
    course_title: str
    teacher_name: str
    grade: float
    enrolled_at: date

@dataclass
class Student:
    email: str
    full_name: str
    group_name: str
    id: int | None = None

@dataclass
class Course:
    code: str
    title: str
    teacher_name: str
    id: int | None = None

@dataclass
class Enrollment:
    student_id: int
    course_id: int
    grade: float
    enrolled_at: date
    id: int | None = None

@dataclass
class ImportReport:
    processed: int = 0
    created_students: int = 0
    created_courses: int = 0
    created_enrollments: int = 0
    updated_enrollments: int = 0
