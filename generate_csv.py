import csv
import random
from datetime import date, timedelta
from pathlib import Path

FIRST_NAMES = [
    "Andrii", "Oleh", "Maksym", "Taras", "Ivan", "Nazar", "Yurii", "Roman",
    "Olena", "Iryna", "Sofiia", "Marta", "Anastasiia", "Kateryna", "Viktoriia", "Solomiia"
]

LAST_NAMES = [
    "Savchuk", "Koval", "Melnyk", "Bondarenko", "Tkachenko", "Shevchenko",
    "Boyko", "Kravets", "Lytvyn", "Mazur", "Kozak", "Polishchuk"
]

GROUPS = ["IPZ-21", "IPZ-22", "KN-21", "KN-22", "CS-21", "CS-22", "SE-21", "SE-22"]

COURSES = [
    ("CS101", "Algorithms", "Oleh Koval"),
    ("CS102", "Databases", "Iryna Hnatiuk"),
    ("CS103", "Computer Networks", "Taras Melnyk"),
    ("CS104", "Operating Systems", "Roman Boyko"),
    ("CS105", "Software Engineering", "Marta Kravets"),
    ("CS106", "Web Development", "Anastasiia Lytvyn"),
    ("CS107", "Cloud Computing", "Nazar Polishchuk"),
    ("CS108", "Data Structures", "Olena Mazur"),
    ("CS109", "Machine Learning", "Kateryna Kozak"),
    ("CS110", "Cybersecurity", "Viktoriia Bondarenko")
]

def build_students(count: int):
    random.seed(42)
    students = []
    for i in range(1, count + 1):
        first_name = random.choice(FIRST_NAMES)
        last_name = random.choice(LAST_NAMES)
        students.append({
            "student_email": f"{first_name.lower()}.{last_name.lower()}{i}@example.com",
            "student_full_name": f"{first_name} {last_name}",
            "group_name": random.choice(GROUPS)
    })
    return students

def main():
    random.seed(42)
    Path("data").mkdir(exist_ok=True)
    students = build_students(400)
    start_date = date(2023, 9, 1)

    with open("data/input.csv", "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "student_email",
            "student_full_name",
            "group_name",
            "course_code",
            "course_title",
            "teacher_name",
            "grade",
            "enrolled_at"
        ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(1500):
            student = random.choice(students)
            course_code, course_title, teacher_name = random.choice(COURSES)
            enrolled_at = (start_date + timedelta(days=random.randint(0, 700))).isoformat()
            grade = round(random.uniform(60, 100), 2)

            writer.writerow({
                "student_email": student["student_email"],
                "student_full_name": student["student_full_name"],
                "group_name": student["group_name"],
                "course_code": course_code,
                "course_title": course_title,
                "teacher_name": teacher_name,
                "grade": grade,
                "enrolled_at": enrolled_at
            })

    print("Generated data/input.csv with 1500 rows")

if __name__ == "__main__":
    main()
