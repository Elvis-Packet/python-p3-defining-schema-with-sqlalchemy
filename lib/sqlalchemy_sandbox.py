#!/usr/bin/env python3

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base
Base = declarative_base()

# Define the Student model
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())

# Database setup
engine = create_engine('sqlite:///students.db')
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Insert student records
def insert_students():
    student1 = Student(name="Alice", age=22)
    student2 = Student(name="Bob", age=24)
    student3 = Student(name="Angela", age=25)

    session.add_all([student1, student2, student3])
    session.commit()
    print(" Students added successfully!")

# Query all students
def query_students():
    students = session.query(Student).all()
    for student in students:
        print(f" ID: {student.id}, Name: {student.name}, Age: {student.age}")

# Update a student's age
def update_student(name, new_age):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        student.age = new_age
        session.commit()
        print(f"Updated {name}'s age to {new_age}!")
    else:
        print(f"⚠️ Student {name} not found.")

# Delete a student
def delete_student(name):
    student = session.query(Student).filter_by(name=name).first()
    if student:
        session.delete(student)
        session.commit()
        print(f" Deleted {name} from the database!")
    else:
        print(f"⚠️ Student {name} not found.")

# Run the functions
if __name__ == '__main__':
    insert_students()
    query_students()
    update_student("Angela", 23)
    delete_student("Alice")
    query_students()  # Show remaining students
