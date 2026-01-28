#Day 4 — Error Handling & Clean Code
#Handle division by zero
#def function
"""def division():
   #input
   try:
      num1=int(input("Enter Number1: ").strip())
      num2=int(input("Enter Number 2: ").strip())
      #solve
      result=num1/num2 
      #output
      print(f"Result: {result}")
   except ZeroDivisionError:
      print("Error: Division By zero not allowed.")
   except ValueError:
      print("Invalid Input,Allow only Integers.")
division()"""
#Handle invalid input (string instead of number)
#def function
"""def invalid():
    #input
    try:
      number=int(input("Enter Number: ").strip())
      print(number)
    except ValueError:
       print("Invalid input,allow only integers.")
invalid()"""
#Safe average calculator
#def calculator
def calculator():
    #input
    while True:
     try:
        num1=int(input("Enter Number 1: ").strip())
        num2=int(input("Enter Number 2: ").strip())
        operator=input("Enter Operation (+,-,/,*) or quit: ").strip().lower()
        if operator == 'quit':
            print('Exiting----')
            break
        operation={
           '+': num1 + num2,
           '-': num1 - num2,
           '*': num1 * num2,
           '/': num1 / num2 if num2!=0 else 'Error: Division By Zero'
        }
        print(f"Result: {operation.get(operator, 'invalid operator')}")
     except ValueError:
        print("Invalid Input, Allow only Integers.")

calculator()