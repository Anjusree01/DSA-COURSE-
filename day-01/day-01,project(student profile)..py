#Student profile command line Interface

student_id = ""
name= ""
age = ""
course = ""

while True:
    print("----------Student Profile Menu------------")
    print("1. Add students")
    print("2. View students")
    print("3. Update students")
    print("4. Delete students")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter age: ")
        course = input("Enter course: ")

        print("Student added Successfully")

    elif choice == "2":
        if student_id == "":
            print("No student found")
        else:
            print("\nStudent Details")
            print("ID: ", student_id)
            print("Name: ", name)
            print("Age: ", age)
            print("Course: ", course)

    elif choice == "3":
        if student_id == "":
            print("No student  found to update")
        else:
            name = input("Enter Name: ")
            age = input("Enter age: ")
            course = input("Enter course: ")
            print("Student updated Succesfully")

    elif choice == "4":
        if student_id == "":
            print("No student found to Delete")
        else:
            student_id = ""
            name = ""
            age = ""
            course = ""
            print("Student Deleted")
    elif choice == "5":
        print("Program Exited")
        break
    else:
        print("Invalid Choice")
