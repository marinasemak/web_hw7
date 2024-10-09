from pprint import pprint

from sqlalchemy import and_, desc, distinct, func

from conf.db import session
from conf.models import Grade, Group, Lecturer, Student, Subject


def select_1():
    result = (
        session.query(
            Student.id,
            Student.fullname,
            func.round(func.avg(Grade.grade_value), 0).label("average_grade"),
        )
        .select_from(Student)
        .join(Grade)
        .group_by(Student.id)
        .order_by(desc("average_grade"))
        .limit(5)
        .all()
    )

    return result


def select_2():
    result = (
        session.query(
            Student.id,
            Student.fullname,
            Subject.name,
            func.round(func.avg(Grade.grade_value), 0).label("average_grade"),
        )
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .filter(Subject.name == "Geophysics")
        .group_by(Student.id)
        .group_by(Subject.id)
        .order_by(desc("average_grade"))
        .first()
    )
    return result


def select_3():
    result = (
        session.query(
            Group.name,
            Subject.name,
            func.round(func.avg(Grade.grade_value), 0).label("average_grade"),
        )
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .join(Group)
        .filter(Subject.name == "Mathematics")
        .group_by(Student.group_id)
        .group_by(Subject.id)
        .group_by(Group.id)
        .order_by(desc("average_grade"))
        .first()
    )
    return result


def select_4():
    result = (
        session.query(
            func.round(func.avg(Grade.grade_value), 0).label("average_grade"),
        )
        .select_from(Grade)
        .scalar()
    )
    return result


def select_5():
    result = (
        session.query(
            Lecturer.name,
            Subject.name,
        )
        .select_from(Lecturer)
        .join(Subject)
        .filter(Lecturer.name == "Douglas Garcia")
        .all()
    )
    return result


def select_6():
    result = (
        session.query(
            Student.fullname,
            Group.name,
        )
        .select_from(Student)
        .join(Group)
        .filter(Group.name == "GroupA")
        .all()
    )
    return result


def select_7():
    result = (
        session.query(
            Student.fullname,
            Grade.grade_value,
            Subject.name,
            Group.name,
        )
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .join(Group)
        .filter(and_(Subject.name == "Geophysics"), (Group.name == "GroupC"))
        .all()
    )
    return result


def select_8():
    result = (
        session.query(
            Lecturer.name,
            Subject.name,
            func.round(func.avg(Grade.grade_value), 0).label("average_grade"),
        )
        .select_from(Lecturer)
        .join(Subject)
        .join(Grade)
        .filter(Lecturer.name == "Douglas Garcia")
        .group_by(Lecturer.name)
        .group_by(Subject.name)
        .first()
    )
    return result


def select_9():
    result = (
        session.query(
            distinct(Student.id),
            Student.fullname,
            Subject.name,
        )
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .filter(Student.fullname == "Summer Williams")
        .all()
    )
    return result


def select_10():
    result = (
        session.query(
            distinct(Student.id), Student.fullname, Subject.name, Lecturer.name
        )
        .select_from(Student)
        .join(Grade)
        .join(Subject)
        .join(Lecturer)
        .filter(
            and_(Student.fullname == "Summer Williams"),
            (Lecturer.name == "Douglas Garcia"),
        )
        .all()
    )
    return result


if __name__ == "__main__":

    pprint(select_10())
