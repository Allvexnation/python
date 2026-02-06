from datetime import datetime

students = []

def search_student(keyword):
    results = []
    for s in students:
        if s["id"].lower() == keyword.lower() or s["name"].lower() == keyword.lower():
            results.append(s)
    return results


while True:
    print("\n============== STUDENT MANAGEMENT SYSTEM ==============")
    print(
        "1. Add Students\n"
        "2. View Students\n"
        "3. Search Students\n"
        "4. Update Student\n"
        "5. Delete Students\n"
        "6. Exit"
    )
    
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))

        year = datetime.now().strftime("%y")
        count = len(students) + 1
        student_id = f"CCA{year}{count:04d}"

        students.append({
            "id": student_id,
            "name": name,
            "age": age
        })

        print("Student Added with ID:", student_id)

    elif choice == "2":
        if not students:
            print("No Students found")
        else:
            for s in students:
                print("ID:", s["id"], "Name:", s["name"], "Age:", s["age"])

    elif choice == "3":
        keyword = input("Enter student ID or Name: ")
        results = search_student(keyword)

        if results:
            for s in results:
                print("Found -> ID:", s["id"], "Name:", s["name"], "Age:", s["age"])
        else:
            print("No student found")

    elif choice == "4":
        keyword = input("Enter student ID or Name to update: ")
        results = search_student(keyword)

        if not results:
            print("Student not found")
        else:
            student = results[0]
            print("Current Data:", student)

            new_name = input("Enter new name (leave blank to keep current): ")
            new_age = input("Enter new age (leave blank to keep current): ")

            if new_name:
                student["name"] = new_name
            if new_age:
                student["age"] = int(new_age)

            print("Student updated successfully")

    elif choice == "5":
        keyword = input("Enter student ID or Name to delete: ")
        before = len(students)

        students = [
            s for s in students
            if s["id"].lower() != keyword.lower()
            and s["name"].lower() != keyword.lower()
        ]

        if len(students) < before:
            print("Student deleted successfully")
        else:
            print("Student not found")

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
