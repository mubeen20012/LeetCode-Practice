#Day 6 — Tuples & Sets
#Find unique values in dataset
#def function
def unique():
    num=[]
    #take input
    numbers=[1,2,3,4,5,6,5,4,3,6,1]
    #solve
    for number in numbers:
        if number not in num:
            num.append(number)        
    #output
    print(num)
unique()
#Remove duplicates using set
#def fubction
def duplicate():
    unique=[]
    #take input
    numbers=[1,2,3,4,5,6,7,6,5]
    #solve
    for num in numbers:
        if num not in unique:
            unique.append(num)
    #output
    print(unique)
duplicate()
number=[1,2,3,4,5,6,7,6,5]
numbers=set(number)
print(numbers)
#Find common elements between two lists
#def function
def common():
   numbers=[]
   #take input
   num1=[1,2,3,4,5]
   num2=[4,5,6,7,8]
   #solve
   for n in num1:
       if n in num2:
           numbers.append(n)
   #output
   print(numbers)
common()



