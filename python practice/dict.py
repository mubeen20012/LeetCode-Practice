"""#📌 Project: Student Record Manager
def record():
    students={}
    while True:
        print("\nStudent Record Manager")
        print("1. Add Student")
        print("2. View Student")        
        print("3. Update Student")
        print("4. Delete Student")
        print('5. Show Topper')
        print("0. Exit")
        try:
            choice=int(input("Enter Your Choice: ").strip())
            if choice==1:
                print("Add Students")
                name=input("Enter Your name: ").strip().title()
                try:
                   marks=int(input("Enter Your Marks: ").strip())
                except ValueError:
                    print("Invalid Input,Allow only Integers.")
                    return
                if name in students:
                    print("Student Already Exists.")
                else:   
                    students[name]=marks
                    print("Student Added Successfully.")
            elif choice==2:
                print("View Students")
                for name,marks in students.items():
                    print(f"{name} : {marks}")
            elif choice==3:
                print("Update Students")
                name=input('Enter Student Name: ').strip().title()
                new_marks=int(input('Enter Student Marks: ').strip())
                students[name]=new_marks
            elif choice==4:
                name=input("Enter student name to delete: ").strip().title()
                if name in students:
                   del students[name]
                   print("Student Deleted Successfully.")
                else:
                    print("Student Not Found.")
            elif choice==5:
                print("Show Topper")
                topper=max(students,key=students.get)
            elif choice==0:
                print("Exiting----")
                break
            else:
                print("Invalid Choice.")
        except ValueError:
            print("Invalid Input,Allow only Integers.")
record()"""

