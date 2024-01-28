import sys
# import student_management_logic

def add_student():
    """Add a new student to the dictionary."""
    student_id = input("Enter student ID: ")
    if student_id in students:
        print("Student already exists.")
        return
    first_name = input("Enter first name: ")
    while not first_name.isalpha():
        print("Invalid input. Enter a valid name.")
        first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    while not last_name.isalpha():
        print("Invalid input. Enter a valid name.")
        last_name = input("Enter last name: ")
    contact_number = input("Enter contact number: ")
    while not contact_number.isdigit() or len(contact_number) != 10:
        print("Invalid input. Enter a valid 10-digit contact number.")
        contact_number = input("Enter contact number: ")
    marks1 = float(input("Enter marks for subject 1: "))
    marks2 = float(input("Enter marks for subject 2: "))
    students[student_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "contact_number": contact_number,
        "marks": {"subject1": marks1, "subject2": marks2}
    }
    print("Student added successfully.")

def remove_student():
    """Remove a student from the dictionary."""
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found.")
        return
    del students[student_id]
    print("Student removed successfully.")

def view_all_students():
    """Display all students in the dictionary."""
    if not students:
        print("No students found.")
        return
    print("ID\tFirst Name\tLast Name\tContact Number\tSubject 1\tSubject 2")
    for student_id, student_details in students.items():
        print(f"{student_id}\t{student_details['first_name']}\t{student_details['last_name']}\t{student_details['contact_number']}\t{student_details['marks']['subject1']}\t{student_details['marks']['subject2']}")

def view_specific_student():
    """Display a specific student by ID."""
    student_id = input("Enter student ID: ")
    if student_id not in students:
        print("Student not found.")
        return
    student_details = students[student_id]
    print(f"ID: {student_id}")
    print(f"First Name: {student_details['first_name']}")
    print(f"Last Name: {student_details['last_name']}")
    print(f"Contact Number: {student_details['contact_number']}")
    print(f"Subject 1 Marks: {student_details['marks']['subject1']}")
    print(f"Subject 2 Marks: {student_details['marks']['subject2']}")

def main():
    """Main function to display the menu and call the appropriate functions."""
    global students
    students = {}
    while True:
        print("\nStudent Management System")
        print("1. Add student")
        print("2. Remove student")
        print("3. View all students")
        print("4. View specific student")
        print("5. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            add_student()
        elif option == 2:
            remove_student()
        elif option == 3:
            view_all_students()
        elif option == 4:
            view_specific_student()
        elif option == 5:
            sys.exit(0)
        else:
            print("Invalid option. Please enter a valid option.")

if __name__ == "__main__":
    main()