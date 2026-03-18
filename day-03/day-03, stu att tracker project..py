#student attendence tracker
student_name=""
student_status=""
def show_menu():
    print("1.add attendance")
    print("2.View attendance")
    print("3.Exit")

def add_attendance():
    global student_name
    global student_status
    student_name=input("Enter name: ")
    student_status=input("Enter status present/absent: ")
    print("Attendance added successfully.")

def view_attendance():
    if student_name=="":
        print("No record found")
    else:
        print("Attendance record")
        print(student_name ,"--",student_status)

def main():
    while True:
        show_menu()
        choice=input("Enter your choice: ")
        if choice=='1':
            add_attendance()
        elif choice=='2':
            view_attendance()
        elif choice=='3':
            print("Exit")
            break
        else:
            print("Invalid choice")
main()
