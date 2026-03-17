from src.business.services import ImportService
from src.config import load_settings
from src.data_access.file_reader import CsvEnrollmentFileReader
from src.data_access.orm_models import StudentORM, CourseORM, EnrollmentORM
from src.data_access.repositories import (
    SqlAlchemyStudentRepository,
    SqlAlchemyCourseRepository,
    SqlAlchemyEnrollmentRepository,
    SqlAlchemyUnitOfWork,
)
from src.db import Base, create_session_factory

def build_import_service():
    settings = load_settings()
    engine, session_factory = create_session_factory(settings.database_url)

    _ = (StudentORM, CourseORM, EnrollmentORM)

    Base.metadata.create_all(engine)
    session = session_factory()

    service = ImportService(
        file_reader=CsvEnrollmentFileReader(),
        student_repository=SqlAlchemyStudentRepository(session),
        course_repository=SqlAlchemyCourseRepository(session),
        enrollment_repository=SqlAlchemyEnrollmentRepository(session),
        unit_of_work=SqlAlchemyUnitOfWork(session)
    )

    return service, session
