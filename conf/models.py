from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import (
    create_engine,
    Integer,
    String,
    Date,
    ForeignKey,
    select,
    Text,
    and_,
    desc,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)

    student = relationship("Student", back_populates="group")


class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    last_name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    group_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("groups.id", onupdate="CASCADE", ondelete="SET NULL")
    )

    group = relationship("Group", back_populates="student")
    grade = relationship("Grade", back_populates="student")

    @hybrid_property
    def fullname(self):
        return self.first_name + " " + self.last_name


class Lecturer(Base):
    __tablename__ = "lecturers"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)

    subject = relationship("Subject", back_populates="lecturer")


class Subject(Base):
    __tablename__ = "subjects"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(120), nullable=False, index=True)
    lecturer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("lecturers.id", onupdate="CASCADE", ondelete="SET NULL")
    )

    lecturer = relationship("Lecturer", back_populates="subject")
    grade = relationship("Grade", back_populates="subject")


class Grade(Base):
    __tablename__ = "grades"
    id: Mapped[int] = mapped_column(primary_key=True)
    grade_value: Mapped[int]
    student_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("students.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    subject_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("subjects.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    date: Mapped[datetime] = mapped_column(Date, nullable=False)

    student = relationship("Student", back_populates="grade")
    subject = relationship("Subject", back_populates="grade")
