from src.container import build_import_service

def main():
    service, session = build_import_service()
    try:
        report = service.import_from_csv("data/input.csv")
        print(f"Processed rows: {report.processed}")
        print(f"Created students: {report.created_students}")
        print(f"Created courses: {report.created_courses}")
        print(f"Created enrollments: {report.created_enrollments}")
        print(f"Updated enrollments: {report.updated_enrollments}")
    finally:
        session.close()

if __name__ == "__main__":
    main()
