from sqlalchemy.orm import joinedload

from conf.db import session
from conf.models import Grade, Group, Lecturer, Student, Subject

# Command examples
#  py main.py -a create -m Teacher -n 'Boris Jonson'
#  py main.py -a create -m Group -n 'AD-101'

# CRUD
# --action create -m Teacher --name 'Boris Jonson' створення вчителя
# --action list -m Teacher показати всіх вчителів
# --action update -m Teacher --id 3 --name 'Andry Bezos' оновити дані вчителя з id=3
# --action remove -m Teacher --id 3 видалити вчителя з id=3


def create_group(name):
    groups = Group(name=name)
    session.add(groups)
    session.commit()
    print("The group was added")


def update_group(g_id, new_name):
    group = session.query(Group).filter_by(id=g_id).first()
    group.name = new_name
    session.commit()
    print("The group was updated")


def list_group():
    groups = session.query(Group).all()
    for g in groups:
        columns = ["id", "group_name"]
        r = [dict(zip(columns, (g.id, g.name)))]
        print(r)


def delete_group(g_id):
    group = session.query(Group).filter_by(id=g_id).first()
    session.delete(group)
    session.commit()
    print("The group was deleted")


def create_student(first_name, last_name, g_id):
    student = Student(first_name=first_name, last_name=last_name, group_id=g_id)
    session.add(student)
    session.commit()
    print("The student was added")


def update_student(s_id, new_first_name, new_last_name, g_id):
    student = session.query(Student).filter_by(id=s_id).first()
    student.first_name = new_first_name
    student.last_name = new_last_name
    student.group_id = g_id
    session.commit()
    print("The student was updated")


def list_students():
    students = session.query(Student).options(joinedload(Student.group)).all()
    for s in students:
        columns = ["id", "fullname", "group_id", "group_name"]
        r = [dict(zip(columns, (s.id, s.fullname, s.group_id, s.group.name)))]
        print(r)


def delete_student(s_id):
    student = session.query(Student).filter_by(id=s_id).first()
    session.delete(student)
    session.commit()
    print("The student was deleted")


def create_lecturer(l_name):
    lecturer = Lecturer(name=l_name)
    session.add(lecturer)
    session.commit()
    print("The lecturer was added")


def update_lecturer(l_id, new_l_name):
    lecturer = session.query(Lecturer).filter_by(id=l_id).first()
    lecturer.name = new_l_name
    session.commit()
    print("The lecturer was updated")


def list_lecturer():
    lecturers = session.query(Lecturer).all()
    for l in lecturers:
        columns = ["id", "lecturer_name"]
        r = [dict(zip(columns, (l.id, l.name)))]
        print(r)


def delete_lecturer(l_id):
    lecturer = session.query(Lecturer).filter_by(id=l_id).first()
    session.delete(lecturer)
    session.commit()
    print("The lecturer was deleted")


def create_subject(subject_name, l_id):
    subjects = Subject(name=subject_name, lecturer_id=l_id)
    session.add(subjects)
    session.commit()
    print("The subject was added")


def update_subject(sb_id, new_subject_name, l_id):
    subject = session.query(Subject).filter_by(id=sb_id).first()
    subject.name = new_subject_name
    subject.lecturer_id = l_id
    session.commit()
    print("The subject was updated")


def list_subjects():
    subjects = session.query(Subject).options(joinedload(Subject.lecturer)).all()
    for sb in subjects:
        columns = ["id", "subject", "lecturer_name"]
        r = [dict(zip(columns, (sb.id, sb.name, sb.lecturer.name)))]
        print(r)


def delete_subject(sb_id):
    subject = session.query(Subject).filter_by(id=sb_id).first()
    session.delete(subject)
    session.commit()
    print("The subject was deleted")


def create_grade(grade, s_id, sb_id, date):
    grade = Grade(
        grade_value=grade,
        student_id=s_id,
        subject_id=sb_id,
        date=date,
    )
    session.add(grade)
    session.commit()
    print("The grade was added")


def update_grade(gr_id, new_grade, date):
    grade = session.query(Grade).filter_by(id=gr_id).first()
    grade.grade_value = new_grade
    grade.date = date
    session.commit()
    print("The grade was updated")


def list_grades():
    grades = (
        session.query(Grade)
        .options(joinedload(Grade.student).joinedload(Grade.subject))
        .all()
    )
    for gr in grades:
        columns = ["id", "grade", "student_name", "subject"]
        r = [
            dict(
                zip(
                    columns,
                    (gr.id, gr.grade_value, gr.student.fullname, gr.subject.name),
                )
            )
        ]
        print(r)


def delete_grade(gr_id):
    grade = session.query(Grade).filter_by(id=gr_id).first()
    session.delete(grade)
    session.commit()
    print("The grade was deleted")
