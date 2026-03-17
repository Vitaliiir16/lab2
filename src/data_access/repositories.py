from sqlalchemy import select
from sqlalchemy.orm import Session
from src.data_access.mappers import to_student, to_course, to_enrollment
from src.data_access.orm_models import StudentORM, CourseORM, EnrollmentORM
from src.domain.interfaces import IStudentRepository, ICourseRepository, IEnrollmentRepository, IUnitOfWork
from src.domain.models import Student, Course, Enrollment

class SqlAlchemyStudentRepository(IStudentRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_email(self, email: str) -> Student | None:
        entity = self.session.execute(
            select(StudentORM).where(StudentORM.email == email)
        ).scalar_one_or_none()
        return to_student(entity) if entity else None

    def save(self, student: Student) -> Student:
        if student.id is None:
            entity = StudentORM(
                email=student.email,
                full_name=student.full_name,
                group_name=student.group_name
            )
            self.session.add(entity)
            self.session.flush()
            return to_student(entity)

        entity = self.session.get(StudentORM, student.id)
        entity.email = student.email
        entity.full_name = student.full_name
        entity.group_name = student.group_name
        self.session.flush()
        return to_student(entity)

class SqlAlchemyCourseRepository(ICourseRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_code(self, code: str) -> Course | None:
        entity = self.session.execute(
            select(CourseORM).where(CourseORM.code == code)
        ).scalar_one_or_none()
        return to_course(entity) if entity else None

    def save(self, course: Course) -> Course:
        if course.id is None:
            entity = CourseORM(
                code=course.code,
                title=course.title,
                teacher_name=course.teacher_name
            )
            self.session.add(entity)
            self.session.flush()
            return to_course(entity)

        entity = self.session.get(CourseORM, course.id)
        entity.code = course.code
        entity.title = course.title
        entity.teacher_name = course.teacher_name
        self.session.flush()
        return to_course(entity)

class SqlAlchemyEnrollmentRepository(IEnrollmentRepository):
    def __init__(self, session: Session):
        self.session = session

    def get_by_student_and_course(self, student_id: int, course_id: int) -> Enrollment | None:
        entity = self.session.execute(
            select(EnrollmentORM).where(
                EnrollmentORM.student_id == student_id,
                EnrollmentORM.course_id == course_id
            )
        ).scalar_one_or_none()
        return to_enrollment(entity) if entity else None

    def save(self, enrollment: Enrollment) -> Enrollment:
        if enrollment.id is None:
            entity = EnrollmentORM(
                student_id=enrollment.student_id,
                course_id=enrollment.course_id,
                grade=enrollment.grade,
                enrolled_at=enrollment.enrolled_at
            )
            self.session.add(entity)
            self.session.flush()
            return to_enrollment(entity)

        entity = self.session.get(EnrollmentORM, enrollment.id)
        entity.student_id = enrollment.student_id
        entity.course_id = enrollment.course_id
        entity.grade = enrollment.grade
        entity.enrolled_at = enrollment.enrolled_at
        self.session.flush()
        return to_enrollment(entity)

class SqlAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self, session: Session):
        self.session = session

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()
