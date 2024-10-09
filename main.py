import argparse
import logging
from datetime import date

from sqlalchemy.exc import SQLAlchemyError

import db_crud as crud
from conf.db import session

# Command examples
#  py main.py -a create -m Teacher -n 'Boris Jonson'
#  py main.py -a create -m Group -n 'AD-101'
parser = argparse.ArgumentParser(description="Example CLI using argparse")
parser.add_argument(
    "-a", "--action", type=str, help="Enter CRUD command: create/list/update/remove"
)
parser.add_argument("-m", "--model", type=str, help="Table to modify")
parser.add_argument("-n", "--name", type=str, help="Name")
parser.add_argument("--id", type=int, help="object ID")
parser.add_argument("--rel", type=int, help="relative ID")
parser.add_argument("--rel2", type=int, help="2nd relative ID")
parser.add_argument("-g", "--grade", type=int, help="student grade")

action = parser.parse_args().action
model = parser.parse_args().model
name = parser.parse_args().name
obj_id = parser.parse_args().id
rel_id = parser.parse_args().rel
rel2_id = parser.parse_args().rel2
grade = parser.parse_args().grade


def handle_groups(action, name=None, obj_id=None):
    match action:
        case "create":
            crud.create_group(name)
        case "update":
            crud.update_group(obj_id, name)
        case "list":
            crud.list_group()
        case "remove":
            crud.delete_group(obj_id)


def handle_students(action, name=None, obj_id=None, rel_id=None):
    match action:
        case "create":
            first_name, last_name = name.split()
            crud.create_student(first_name, last_name, rel_id)
        case "update":
            new_first_name, new_last_name = name.split()
            crud.update_student(obj_id, new_first_name, new_last_name, rel_id)
        case "list":
            crud.list_students()
        case "remove":
            crud.delete_student(obj_id)


def handle_subjects(action, name=None, obj_id=None, rel_id=None):
    match action:
        case "create":
            crud.create_subject(name, rel_id)
        case "update":
            crud.update_subject(obj_id, name, rel_id)
        case "list":
            crud.list_subjects()
        case "remove":
            crud.delete_subject(obj_id)


def handle_lecturers(action, name=None, obj_id=None):
    match action:
        case "create":
            crud.create_lecturer(name)
        case "update":
            crud.update_lecturer(obj_id, name)
        case "list":
            crud.list_lecturer()
        case "remove":
            crud.delete_lecturer(obj_id)


def handle_grades(action, grade=None, obj_id=None, rel_id=None, rel2_id=None):
    grade_date = date.today()
    match action:
        case "create":
            crud.create_grade(grade, rel_id, rel2_id, grade_date)
        case "update":
            crud.update_grade(obj_id, grade, grade_date)
        case "list":
            crud.list_grades()
        case "remove":
            crud.delete_grade(obj_id)


def main(action, model):
    # command, *args = parse_input(user_input)

    match model:
        case "Group":
            handle_groups(action, name, obj_id)
        case "Student":
            handle_students(action, name, obj_id, rel_id)
        case "Subject":
            handle_subjects(action, name, obj_id, rel_id)
        case "Lecturer":
            handle_lecturers(action, name, obj_id)
        case "Grade":
            handle_grades(action, grade, obj_id, rel_id, rel2_id)
        case _:
            print("Invalid command.")


if __name__ == "__main__":
    try:
        main(action, model)
    except SQLAlchemyError as e:
        logging.error(e)
        session.rollback()
    finally:
        session.close()
