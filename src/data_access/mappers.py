from src.domain.models import Student, Course, Enrollment
from src.data_access.orm_models import StudentORM, CourseORM, EnrollmentORM

def to_student(entity: StudentORM) -> Student:
    return Student(
        id=entity.id,
        email=entity.email,
        full_name=entity.full_name,
        group_name=entity.group_name
    )

def to_course(entity: CourseORM) -> Course:
    return Course(
        id=entity.id,
        code=entity.code,
        title=entity.title,
        teacher_name=entity.teacher_name
    )

def to_enrollment(entity: EnrollmentORM) -> Enrollment:
    return Enrollment(
        id=entity.id,
        student_id=entity.student_id,
        course_id=entity.course_id,
        grade=entity.grade,
        enrolled_at=entity.enrolled_at
    )
