#Day 4
#Function to calculate mean of a list
#def function
"""def mean_list():
    #declare list
    numbers=[1,2,3,4,5]
    count=0
    #solve
    for num in numbers:
        count=count+ num
    average=count/len(numbers)
    #output
    print(f"Average: {average}")
mean_list()"""
#Function to check prime number
#def function
"""def number():
    try:
        number=int(input("Enter Number: ").strip())
        if number <=1:
            print(f'Number {number} is not a prime.')
            return
        for i in range(2,number):
            if number%i==0:
                print(f'Number {number} is not a prime.')
                return
        print(f'Number {number} is  a prime.')

    except ValueError:
        print("Invalid Input,Allow only Integers.")
number()"""
#Function that returns min & max from list
#def function
"""def numbers():
   #list declare
   numbers=[1,2,3,4,5]
   largest=numbers[0]
   smallest=numbers[0]
   #solve
   for num in numbers:
      if num > largest:
         largest=num
      if num < smallest:
         smallest=num
   #output
   print(f"Smallest: {smallest}")
   print(f"Largest: {largest}")
numbers()"""
#Function to clean string (lowercase + remove spaces)
#def function
"""def clean():
     #input
     name=input("Enter Name: ").strip().lower()
     #solve
     final=name.replace(" ","")
     #output
     print(f"Name: {final}")
clean()"""
#Write a function with docstring for data cleaning
def data_clean(data):
    clean_data=[]
    for item in data:
        if type(item)==str:
            item=item.lower()
            item=item.strip()
            clean_data.append(item)
        else:
            clean_data.append('')
    return clean_data 
data = ["  Hello   World ", " PYTHON Data   Science ", None]
result=data_clean(data)
print(result)


      
