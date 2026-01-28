#day7
#Find common elements between two lists
#def function
"""def common():
    number=[]
    #take input
    num1=[1,2,3,4,5]
    num2=[5,3,6,7,8]
    #solve
    for num in num1:
        if num in num2:
            number.append(num)
    #output
    print(f"Common Numbers: {number} ")
common()"""
#Convert tuple → list → tuple
"""def num():
    number=(1,2,3,4)
    numbers=list(number)
    numbers.append(5)
    number=tuple(numbers)
    print(number)
num()"""
#Count unique words in sentence
#def function
def unique():
    #take input
    sentence=input("Enter Sentence: ").strip().title()
    words=sentence.split()
    unique=[]
    for word in sentence:
        if word not in unique:
            unique.append(word)
    print(f"Count: {unique}")
unique()
    #solve
    #output



    