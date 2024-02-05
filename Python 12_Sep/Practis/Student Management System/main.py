import student_management_logic as sl

print("Hello Welcome to Tops Tecnologys\n")
print("-----------------------------------------------------------")

ch = int(input("press 1 for Counsellor\npress 2 for Faculty\npress 3 for Student\n"))

students = {}

if ch == 1:
    choice = int(input("1. Add Sttudent\n2. Remove Student\n3. View All Student\n4. View Specific Student\n\nEnter a choice by counsellor: "))
    if choice == 1:
        sl.add_student(students)
    elif choice == 2:
        sl.remove_student(students)
    elif choice == 3:
        sl.view_all_students(students)
    elif choice == 4:
        sl.view_specific_student(students)
    else:
        print("Invalid choice.!")
elif ch == 2:
    choice = int(input('1.Add marks to student\n2.View all student\n\nEnter a choice by Faculty: '))