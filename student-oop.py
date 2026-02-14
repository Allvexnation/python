import json
from datetime import datetime as date
import os

FILE = "students.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f) 
        
with open(FILE) as f:
    students = json.load(f)
class Student:
    def __init__(self, name,age,course, grade):
        year = date.now().strftime("%y")
        count = len(students) + 1
        self.student_id = f"CCA{year}{count:04d}"
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
    def to_dict(self):
        return {"student_id": self.student_id, 
                "name": self.name, 
                "age": self.age,
                "course": self.course, 
                "grade": self.grade
                }
    
def save():
    with open(FILE, "w") as f:
        json.dump(students, f, indent=5)

def create():
    name = input("Name: ")
    age = int(input("Age: "))
    course = input("course: ")
    grade = input("Grade: ")
    s = Student(name, age,course, grade )
    students.append(s.to_dict())
    save()
    print(f"Student {s.name} added with ID {s.student_id}!")

def read():
    print("\n--- STUDENTS ---")
    for s in students:
        print(f"ID:{s['student_id']}, Name:{s['name']}, Age:{s['age']},Course: {s['course']}, Grade:{s['grade']}")
    print("-" * 30)

def update():
    sid = input("Enter Student ID to update: ")
    for s in students:
        if s["student_id"] == sid:
            s["name"] = input(f"New name ({s['name']}): ") or s['name']
            s["course"] = input(f"New name ({s['course']}): ") or s['course']
            s["age"] = int(input(f"New age ({s['age']}): ") or s['age'])
            s["grade"] = input(f"New grade ({s['grade']}): ") or s['grade']
            save()
            print("Student updated!")
            return
    print("Student ID not found.")

def delete():
    sid = input("Enter Student ID to delete: ")
    for i, s in enumerate(students):
        if s["student_id"] == sid:
            students.pop(i)
            save()
            print("Student deleted!")
            return
    print("Student ID not found.")
    
while True:
    print("\n--- STUDENT SYSTEM ---")
    print("1. Add Student")
    print("2. List Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Choose: ")

    if choice == "1": create()
    elif choice == "2": read()
    elif choice == "3": update()
    elif choice == "4": delete()
    elif choice == "5": break
    else: print("Invalid choice!")
