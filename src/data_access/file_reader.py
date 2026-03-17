import csv
from datetime import datetime
from src.domain.interfaces import IFileReader
from src.domain.models import CsvEnrollmentRow

class CsvEnrollmentFileReader(IFileReader):
    def read(self, path: str) -> list[CsvEnrollmentRow]:
        rows = []
        with open(path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                rows.append(
                    CsvEnrollmentRow(
                        student_email=row["student_email"].strip().lower(),
                        student_full_name=row["student_full_name"].strip(),
                        group_name=row["group_name"].strip(),
                        course_code=row["course_code"].strip().upper(),
                        course_title=row["course_title"].strip(),
                        teacher_name=row["teacher_name"].strip(),
                        grade=float(row["grade"]),
                        enrolled_at=datetime.strptime(row["enrolled_at"], "%Y-%m-%d").date()
                    )
                )
        return rows
