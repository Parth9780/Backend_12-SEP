def add_student(students_dict):
    """Add a new student to the dictionary."""
    student_id = input("Enter student ID: ")
    if student_id in students_dict:
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
    students_dict[student_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "contact_number": contact_number,
        "marks": {"subject1": marks1, "subject2": marks2}
    }
    print("Student added successfully.")

    k=open('Student.txt','a')
    k.write(f'first_name: {first_name}')
    k.write(f'last: {last_name}')
    k.write(f'contact_number: {contact_number}')
    k.write(f'marks: subject1{marks1}, subject2{marks2}')
    
    print(k)


def remove_student(students_dict):
    """Remove a student from the dictionary."""
    student_id = input("Enter student ID: ")
    if student_id not in students_dict:
        print("Student not found.")
        return
    del students_dict[student_id]
    print("Student removed successfully.")

def view_all_students(students_dict):
    """Display all students in the dictionary."""
    if not students_dict:
        print("No students found")
        
def view_specific_student(students_dict):
    """Display a specific student by ID."""
    student_id = input("Enter student ID: ")
    if student_id not in students_dict:
        print("Student not found.")
        return
    student_details = students_dict[student_id]
    print(f"ID: {student_id}")
    print(f"First Name: {student_details['first_name']}")
    print(f"Last Name: {student_details['last_name']}")
    print(f"Contact Number: {student_details['contact_number']}")
    print(f"Subject 1 Marks: {student_details['marks']['subject1']}")
    print(f"Subject 2 Marks: {student_details['marks']['subject2']}")

