from src.domain.interfaces import IFileReader, IStudentRepository, ICourseRepository, IEnrollmentRepository, IUnitOfWork
from src.domain.models import Student, Course, Enrollment, ImportReport, CsvEnrollmentRow

class ImportService:
    def __init__(
        self,
        file_reader: IFileReader,
        student_repository: IStudentRepository,
        course_repository: ICourseRepository,
        enrollment_repository: IEnrollmentRepository,
        unit_of_work: IUnitOfWork
    ):
        self.file_reader = file_reader
        self.student_repository = student_repository
        self.course_repository = course_repository
        self.enrollment_repository = enrollment_repository
        self.unit_of_work = unit_of_work

    def import_from_csv(self, path: str) -> ImportReport:
        rows = self.file_reader.read(path)
        report = ImportReport()

        try:
            for row in rows:
                self._validate_row(row)
                report.processed += 1

                student = self.student_repository.get_by_email(row.student_email)
                if student is None:
                    student = self.student_repository.save(
                        Student(
                            email=row.student_email,
                            full_name=row.student_full_name,
                            group_name=row.group_name
                        )
                    )
                    report.created_students += 1
                elif student.full_name != row.student_full_name or student.group_name != row.group_name:
                    student.full_name = row.student_full_name
                    student.group_name = row.group_name
                    student = self.student_repository.save(student)

                course = self.course_repository.get_by_code(row.course_code)
                if course is None:
                    course = self.course_repository.save(
                        Course(
                            code=row.course_code,
                            title=row.course_title,
                            teacher_name=row.teacher_name
                        )
                    )
                    report.created_courses += 1
                elif course.title != row.course_title or course.teacher_name != row.teacher_name:
                    course.title = row.course_title
                    course.teacher_name = row.teacher_name
                    course = self.course_repository.save(course)

                enrollment = self.enrollment_repository.get_by_student_and_course(student.id, course.id)
                if enrollment is None:
                    self.enrollment_repository.save(
                        Enrollment(
                            student_id=student.id,
                            course_id=course.id,
                            grade=row.grade,
                            enrolled_at=row.enrolled_at
                        )
                    )
                    report.created_enrollments += 1
                elif enrollment.grade != row.grade or enrollment.enrolled_at != row.enrolled_at:
                    enrollment.grade = row.grade
                    enrollment.enrolled_at = row.enrolled_at
                    self.enrollment_repository.save(enrollment)
                    report.updated_enrollments += 1

            self.unit_of_work.commit()
            return report
        except Exception:
            self.unit_of_work.rollback()
            raise

    def _validate_row(self, row: CsvEnrollmentRow) -> None:
        if not row.student_email:
            raise ValueError("student_email is required")
        if not row.student_full_name:
            raise ValueError("student_full_name is required")
        if not row.group_name:
            raise ValueError("group_name is required")
        if not row.course_code:
            raise ValueError("course_code is required")
        if not row.course_title:
            raise ValueError("course_title is required")
        if not row.teacher_name:
            raise ValueError("teacher_name is required")
        if row.grade < 0 or row.grade > 100:
            raise ValueError("grade must be between 0 and 100")
