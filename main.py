# student management system
students = []
# new student detail for adding in the list
def add_student():
    name = input("Enter student name: ")
    reg_no = input("Enter registration number: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "registration_no": reg_no,
        "branch": branch,
        "marks": marks
    }
    # student added successfully
    students.append(student) #if new student want to add in the list
    print("Student added successfully")

# view the student details in the list
def view_students():
    if len(students) == 0:
        print("Student records is not found.")
        return

    print("\n-- Student Records --")

    #if  student detail is available in the list
    for student in students:
        print("Name:", student["name"])
        print("Registration No:", student["registration_no"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])
        print("---------------------")

# for searching the student detail in the list
def search_student():
    reg_no = input("Enter registration number to search: ")

    #if  student detail is available in the list
    for student in students:
        if student["registration_no"] == reg_no:
            print("\nStudent Found successful")
            print("Name:", student["name"])
            print("Branch:", student["branch"])
            print("Marks:", student["marks"])
            return
# if student detail is not available in the list then
    print("Student is not found.")

# for correction of student marks in the list
def update_student():
    reg_no = input("Enter registration number: ")

    # if student detail is available in the list then we change the marks
    for student in students:
        if student["registration_no"] == reg_no:
            print("Current marks:", student["marks"])

            new_marks = float(input("Enter new marks: "))
            student["marks"] = new_marks

            print("Student record updated successfully")
            return
    #  if student detail is not available in the list then
    print("Student not found.")

# if other student detail add in the list then using the function and delete the student
def delete_student():
    reg_no = input("Enter registration number: ")

    for student in students:
        if student["registration_no"] == reg_no:
            students.remove(student)
            print("Student deleted successfully")
            return
    #  if student detail is not available in the list then
    print("Student is not found.")

# for calculating the grade 
def calculate_grade():
    reg_no = input("Enter registration number: ")

    # if student detail is available in list then check the marks and convert in gread
    for student in students:
        if student["registration_no"] == reg_no:

            marks = student["marks"]

            if marks >= 90:
                grade = "A+"
            elif marks >= 80:
                grade = "A"
            elif marks >= 70:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            elif marks >= 50:
                grade = "D"
            else:
                grade = "F"

            # show the marks and grade
            print("Marks:", marks)
            print("Grade:", grade)
            return
    #  if student detail is not available in the list then
    print("Student not found.")

# using loop for run the code infinite times
while True:

    print("\n==============================")
    print("   STUDENT MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Grade")
    print("7. Exit")

    # choose your any choice
    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        calculate_grade()

    elif choice == "7":
        print("Thank you")
        break
        # if choosing choice is not available in the given choice
    else:
        print("your choice is  invalid")
