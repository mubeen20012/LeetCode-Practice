#Convert string "123.45" into float and add 10.
x="123.45"
y=float(x)
z=y+10
print(z)
#Take user age → print age after 5 years.
#ask user to enter age
try:
    age=int(input("Enter Age: ").strip())
    #multiply age to 5
    final_age=age + 5
    #print answer
    print(f'Age After 5 Years: {final_age}')
except ValueError:
        print("invalid input,allow only integers.")


#Convert temperature Celsius → Fahrenheit (F = C * 9/5 + 32).
def temperature():
    #enter temperature
    try:
        temp=int(input("Enter Temperature: ")
                 .strip())
        #convert temperature to fehrenheit
        f=temp*9/5+32
        #result
        print(f"Celcius to Fehrenheit: {f}")
    except ValueError:
        print('Invalid input,allow only integers.')   
temperature()

#Swap two variables without using a temporary variable.
#enter 1st value
a=5
#enter 2nd value
b=6
#swap
a,b=b,a
#output
print(a)
print(b)
a=5
b=6
c=a
a=b
b=c
print(a)
print(b)
#Print the last digit of a number given by the user.
#enter number
number=int(input("Enter Number: ").strip())
#output
numbers=number % 10
print(numbers)