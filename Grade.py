# Create Dictionary

students={ }

#ADD Data

def Add(name,grade):
    students[name]=grade
    print(f"Added {name} student Data")

#Update

def Update(name,grade):
    if name in students:
        students[name]=grade
        print(f"Update {name} student grade {grade}")
    else:
        print(f"Student with {name} not found")

#Delete

def Delete(name):
    if name in students:
        del students[name]
        print(f"Deleted {name} student data")
    else:
        print(f"Student with {name} not found")

#View

def View():
    if len(students) == 0:
        print("No Student Data Available!")
    else:
        print("\nStudent Data:")
        for name, grade in students.items():
            print(f"Name: {name}, Grade: {grade}")
        print()


#Main Loop
while True:
    print("\n------ STUDENT GRADE MANAGEMENT ------")
    print("1. Add Student Data")
    print("2. Update Student Grade")
    print("3. Delete Student Data")
    print("4. View Student Data")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")
        grade = input("Enter student grade: ")
        Add(name, grade)

    elif choice == 2:
        name = input("Enter student name to update: ")
        grade = input("Enter new grade: ")
        Update(name, grade)

    elif choice == 3:
        name = input("Enter student name to delete: ")
        Delete(name)

    elif choice == 4:
        View()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")



