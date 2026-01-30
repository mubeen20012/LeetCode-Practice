#Day 7 — Dictionaries
#Count frequency of words
#def function
"""def freq():
   #take input
   sentence=input("Enter Sentence: ").strip().lower()
   frequency={}
   #solve
   for word in sentence:
      if word in frequency:
         frequency[word]+=1
      else:
         frequency[word]=1   
   #output
   print(f"Frequency: {frequency}")
freq()"""
#Student marks dictionary → find topper
#def fuction
"""def marks():
  #take input
  students={
    'Ali': 89,
    'Amina':97
}
  #solve
  for name,marks in students.items():
    #output
    print(f"Students Marks: {name} : {marks}")
marks()""" 
#📌 Project: Student Record Manager
#def function
def student_manager():
   #take input
   students={}
   #solve
   while True:
        print("\n1. Add student")
        print("2. Update marks")
        print("3. Delete student")
        print("4. View all students")
        print("5. Exit")
        try:
            choice=int(input("Enter Choice: ").strip())
            if choice==1:
                name=input("Enter Your Name: ").strip()
                try:
                    marks=int(input("Enter Marks: ").strip())
                except ValueError:
                    print("Invalid Input,Allow only Integers.")
                    return
                students[name]=marks
                print('Student Added Successfully.')
            elif choice==2:
                new_marks=int(input("Enter New Marks: ").strip())
                students['name']=new_marks
                print("Students Marks Updated Successfully.")
            elif choice==3:
                del students['Ali']
            elif choice==4:
                for name,marks in students.items():
                    print(f"{name}: {marks}")
        except ValueError:
            print("Invalid Input,Allow only Integers.")
student_manager()         
        
      

