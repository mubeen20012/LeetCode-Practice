#Day 3
#Function to calculate mean of a list
#def function
"""def mean():
  #def list
  numbers=[1,2,3,4,5]
  total=0
  #solution
  for num in numbers:
    total=total+num
  average= total/len(numbers)
  #output
  print(f"Average List: {average}")
mean()"""    
#Function to check prime number
#def function
"""def prime():
    #ask user to enter input
    try:
        number=int(input("Enter Number: ").strip())
        if number <=1:
            print(f"{number} is not a prime number.")
    #solve
        for i in range(2,number):
            if number %i==0:
                print(f"This number {number} is not a prime number.")
                return
        print(f"This number {number} is a prime number.")

    except ValueError:
        print("Invalid Input,allow only integers.")
prime()"""
#Function that returns min & max from list
#def function
"""def find_max():
    #def list
    numbers=[1,2,3,4,5]
    largest=numbers[0]
    smallest=numbers[0]
    #solve
    for num in numbers:
        if num > largest:
            largest=num
        if num < smallest:
            smallest=num
    print(f"Maximum: {largest}")
    print(f"Minimum: {smallest}")

find_max()"""
#Function to clean string (lowercase + remove spaces)
#def function
def remove():
    #ask user to enter string
    name=input("Enter Your Name: ")
    #solve
    final=name.lower().replace(" ","")
    #output
    print(f"Final: {final}")
remove()