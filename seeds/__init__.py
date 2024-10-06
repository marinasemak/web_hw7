import logging
from random import randint
import random
from datetime import date

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select

from conf.db import session
from conf.models import Student, Subject, Group, Lecturer, Grade

fake = Faker()

groups_list = ["GroupA", "GroupB", "GroupC"]
subjects_list = ["Geology", "Geography", "Chemistry", "Geophysics", "Mathematics"]

start_date = date(2023, 9, 1)
end_date = date(2024, 6, 30)


def insert_groups():
    for i in groups_list:
        groups = Group(name=i)
        session.add(groups)


def insert_students():
    groups = session.query(Group).all()
    for _ in range(10):
        student = Student(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            group_id=random.choice(groups).id,
        )
        session.add(student)


def insert_lecturers():
    for _ in range(5):
        lecturer = Lecturer(name=fake.name())
        session.add(lecturer)


def insert_subjects():
    lecturers = session.query(Lecturer).all()
    for i in subjects_list:
        subjects = Subject(name=i, lecturer_id=random.choice(lecturers).id)
        session.add(subjects)


def insert_grades():
    subjects = session.query(Subject).all()
    student_id = session.scalars(select(Student.id)).all()

    for stud_id in student_id:
        for _ in range(20):
            grades = Grade(
                grade_value=randint(60, 100),
                student_id=stud_id,
                subject_id=random.choice(subjects).id,
                date=fake.date_between(start_date, end_date),
            )
            session.add(grades)


if __name__ == "__main__":
    try:
        # insert_groups()
        # insert_students()
        # insert_lecturers()
        # insert_subjects()
        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        logging.error(e)
        session.rollback()
    finally:
        session.close()
