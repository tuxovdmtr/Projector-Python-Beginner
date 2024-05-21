from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
host = os.getenv("host")
database = os.getenv("database")
user = os.getenv("user")
password = os.getenv("password")
port = os.getenv("port")

DATABASE_URI = f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(DATABASE_URI)

Base = declarative_base()

class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    subjects = relationship("Student_Subject", back_populates="student") 


class Subject(Base):
    __tablename__ = "subject"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    students = relationship("Student_Subject", back_populates="subject")
    

class Student_Subject(Base):
    __tablename__ = "student_subject"

    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    subject_id = Column(Integer, ForeignKey("subject.id"), nullable=False)

    student = relationship("Student", back_populates="subjects")
    subject = relationship("Subject", back_populates="students")
    

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

students_info = [
    {"name": "Bae", "age": 18},
    {"name": "Eddy", "age": 21},
    {"name": "Lily", "age": 22},
    {"name": "Jenny", "age": 19}
]

subjects_info = [
    {"name": "English"},
    {"name": "Math"},
    {"name": "Spanish"},
    {"name": "Ukrainian"}
]

students_subjects_info = [
    {"student_id": 1, "subject_id": 1},
    {"student_id": 2, "subject_id": 2},
    {"student_id": 3, "subject_id": 3},
    {"student_id": 4, "subject_id": 4},
    {"student_id": 3, "subject_id": 1},
    {"student_id": 1, "subject_id": 3}
]

for student_info in students_info:
    student = Student(name = student_info["name"], age = student_info["age"])
    session.add(student)

for subject_info in subjects_info:
    subject = Subject(name = subject_info["name"])
    session.add(subject)

for student_subject_info in students_subjects_info:
    student_subject = Student_Subject(student_id = student_subject_info["student_id"], subject_id = student_subject_info["subject_id"])
    session.add(student_subject)

session.commit()

english_students = session.query(Student.name).join(Student_Subject).join(Subject).filter(Subject.name == 'English').all()
print(english_students)
