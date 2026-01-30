#Count unique words in sentence
#def function
"""def unique():
    #take input
    sentence=input("Enter Sentence: ").strip().lower()
    #add empty list
    words=[]
    #solving
    for word in sentence:
        if word not in words:
            words.append(word)
    #output
    words=set(words)
    print(f"Unique Words: {words}")
unique()"""
#Count frequency in sentence
#def function
"""def frequency():
   #take input
   sentence=input("Enter Sentence: ").strip().lower()
   #solve
   freq={}
   for word in sentence.split():
       if word in freq:
           freq[word]+=1
       else:
           freq[word]=1
   #output
   print(f"Frequency Count: {freq}")
frequency()"""
#Count frequency of words
"""def frequency():
   sentence=input("Enter Sentence: ").strip().lower()
   #solve
   freq={}
   for word in sentence:
       if word in freq:
           freq[word]+=1
       else:
           freq[word]=1
   #output
   print(f"Frequency Count: {freq}")
frequency()"""
#Student marks dictionary → find topper
#def function
"""def marks():
   #take input
   students={
      'Ali': 90,
      'Amina':97
   }
   #solve
   for name,mark in students.items():
      #output
      print(f"Name: {name} and Marks: {mark}")
marks()"""
#Convert two lists into dictionary
#def function
def num():
  #take input
  num1=[1,2,3]
  num2=[4,5,6]
  #solve
  numbers={}
  for i in range(len(num1)):
    numbers[num1[i]]=num2[i]
  #output
  print(f"Number: {numbers}")
num()