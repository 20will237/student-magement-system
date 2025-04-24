'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
students = []



def addStudent():
    student_id = int(input("Enter the student Id: "))
    age = int(input("Enter the student age: "))
    grade = str(input("Enter student grade: "))
    name = str(input("Enter student name: "))
    
    student = {
        'student_id': student_id,
        'name': name,
        'age': age,
        'grade': grade
    }
    students.append(student)
    print("Student added successfully")
    print()


def searchStudent():
    stud_id = int(input("Enter the student Id: "))
    for stud in students:
        if stud_id == stud['student_id']:
            print('found')
            print(f"student Id: {stud['student_id']}")
            print(f"student name: {stud['name']}")
            print(f"student age: {stud['age']}")
            print(f"student grade: {stud['grade']}")
            break
    print(f"Student with the Id: {stud_id} not found.")
    print()

def removeStudent():
    stud_id = int(input("Enter the student Id: "))
    for stud in students:
        if stud_id == stud['student_id']:
            students.remove(stud)
            print("Student added successfully.")
            break
    print(f"Student with the Id: {stud_id} not found.")
    print()
def updateStudent():
    stud_id = int(input("Enter the student Id: "))
    for stud in students:
        if stud_id == stud.student_id:
            newId = int(input("Enter the new student Id: "))
            newAge = int(input("Enter the student age: "))
            newGrade = chr(input("Enter the new student grade: "))
            newName = str(input("Enter the new student name: "))
            
            stud['student_id'] = newId
            stud['age'] = newAge
            stud['grade'] = newGrade
            stud['name'] = newName
            
            
    print(f"Student with the Id: {stud_id} was updated successfully.")
    print()


def main():
    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if(choice == 1):
            addStudent()
        elif(choice == 2):
            searchStudent()
        elif(choice == 3):
            updateStudent()
        elif(choice == 4):
            removeStudent()
        elif(choice == 5):
            print("Bye Bye. Exiting....")
            return 0
        else:
            print("Wrong choice.")
            
        


main()

























