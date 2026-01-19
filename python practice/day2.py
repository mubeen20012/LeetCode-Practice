#Day 2
#Check if number is positive, negative, or zero
"""def number():
   #Enter number
   try:
      number=int(input("Enter Number: ").strip())
      #apply condition
      if number >0:
         print(f"Number {number} is Positive.")
      elif number <0:
        print(f"Number {number} is Negative.")
      else:
        print(f"Number {number} is Zero.")
   except ValueError:
      print("Invalid Input,Allow only Integers.")
number()"""
#Print all even numbers between 1–100
"""def even():
  #loop
  for i in range(1,100):
    if i%2==0:    
  #Output
     print(i)
    
even()"""
#Count vowels in a string
"""def vowel():
  count=0
  #vowels
  vowels='AEIOUaeiou'
  #Ask user for input
  name=input("Enter Something: ").strip()
  for ch in name:
    if ch in vowels:
     count+=1
  print(f" Vowels: {count}")
vowel()"""
#Find largest number from a list manually
"""def list():
  numbers=[]
  for number in range(1,21):
    numbers.append(number)
  print(numbers)
  largest=numbers[0]
  for num in numbers:
    if num > largest:
      largest=num
  print(f"Largest Number is: {largest}")
list()
"""
#Reverse a number using loop
num=12345
rev=0
while num >0:
    digit=num%10
    rev=rev *10 + digit
    num=num//10
print(f'Reversed Numbers: {rev}')


