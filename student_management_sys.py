#student management system

student_data = {}

def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter student course: ")
    student_data[name] = [age, course]
    print(f"Student {name} added successfully.")
    
    

def view_student():
    if student_data:
        print("Current students:")
        for name, details in student_data.items():
            print(f"Name: {name}, Age: {details[0]}, Course: {details[1]}")
    else:
        print("No student data available.")

def update_student():
    name = input("Enter student name: ")
    if name in student_data:
        try:
            age = int(input("Enter new student age: "))
        except ValueError:
            print("Invalid age. Please enter a number.")
            return
        course = input("Enter new student course: ")
        student_data[name] = [age, course]
        print(f"Student '{name}' updated successfully.")
    else:
        print(f"Student '{name}' not present!")

def delete():
    delete_student = input("Enter student name to delete:") 
    if delete in student_data:
        del student_data[delete]
        print(f"Student {delete} deleted successfully.")
    else:
        print("student not present in list")


while True:
    print('''Operations 
          1. Add student
          2. View student
          3. Update student
          4. Delete student
          5. Exit
          ''')
    operation=int(input("Enter operation you want to perform:"))

    if operation==1:
        add_student()

    elif operation==2:
        view_student()

    elif operation==3:
        update_student()

    elif operation==4:
        delete()

    elif operation==5:
        print("Exiting...")
        break

    else:
        print("Invalid operation. Please try again.")
