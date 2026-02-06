import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    student_id = input("Enter Student ID: ")
    name = input("Enter Full Name: ")
    course = input("Enter Course/Section: ")
    grade = input("Enter Grade: ")

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "grade": grade
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!\n")


def view_students(students):
    if not students:
        print("No student records found.\n")
        return

    print("\n--- STUDENT LIST ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Course: {s['course']} | Grade: {s['grade']}")
    print()


def search_student(students):
    student_id = input("Enter Student ID to search: ")
    for s in students:
        if s["id"] == student_id:
            print("\nStudent Found:")
            print(f"ID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Course: {s['course']}")
            print(f"Grade: {s['grade']}\n")
            return
    print("Student not found.\n")


def update_student(students):
    student_id = input("Enter Student ID to update: ")
    for s in students:
        if s["id"] == student_id:
            s["name"] = input("Enter new name: ")
            s["course"] = input("Enter new course/section: ")
            s["grade"] = input("Enter new grade: ")
            save_students(students)
            print("Student record updated.\n")
            return
    print("Student not found.\n")


def delete_student(students):
    student_id = input("Enter Student ID to delete: ")
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            save_students(students)
            print("Student deleted successfully.\n")
            return
    print("Student not found.\n")


def main():
    students = load_students()

    while True:
        print("STUDENT RECORD SYSTEM")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")


main()
