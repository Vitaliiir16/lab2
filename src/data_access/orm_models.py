from sqlalchemy import Date, Float, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.db import Base

class StudentORM(Base):
    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    group_name: Mapped[str] = mapped_column(String(100), nullable=False)

    enrollments: Mapped[list["EnrollmentORM"]] = relationship(back_populates="student", cascade="all, delete-orphan")

class CourseORM(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    teacher_name: Mapped[str] = mapped_column(String(255), nullable=False)

    enrollments: Mapped[list["EnrollmentORM"]] = relationship(back_populates="course", cascade="all, delete-orphan")

class EnrollmentORM(Base):
    __tablename__ = "enrollments"
    __table_args__ = (UniqueConstraint("student_id", "course_id", name="uq_student_course"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("students.id"), nullable=False)
    course_id: Mapped[int] = mapped_column(ForeignKey("courses.id"), nullable=False)
    grade: Mapped[float] = mapped_column(Float, nullable=False)
    enrolled_at: Mapped[Date] = mapped_column(Date, nullable=False)

    student: Mapped["StudentORM"] = relationship(back_populates="enrollments")
    course: Mapped["CourseORM"] = relationship(back_populates="enrollments")
