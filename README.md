# Lab 2

Logic: the program creates a CSV file, reads it, and saves the data to a MySQL database.

The project is split into 3 parts:
- data access - is responsible for reading data from the CSV file and saving or retrieving data from the database.
- business logic - is responsible for deciding what the program should do with the data, such as creating new records or updating existing ones.
- presentation -  is responsible for starting the process and showing the result to the user.

The program works with:
- students (email, full name, group)
- courses (code, title, teacher)
- enrollments (srudent, course, grade, enroll_date)

Each row in the CSV file contains data about a student, a course, and the student's enrollment.

When the import starts, the program:
- checks if the student already exists
- checks if the course already exists
- checks if the enrollment already exists
- creates a new record if needed
- updates the old one if it is already in the database

So the program does not just copy everything blindly.
It tries to save the data correctly and avoid unnecessary duplicates.

## Technologies

- Python
- MySQL
- SQLAlchemy

## How to run

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python generate_csv.py
python app.py
