print("WELCOME TO PYTHON QUIZ!!!")
playing=input("DO YOU WANT TO PLAY??")
if playing.lower()!="yes":
    quit()
print("OKAY!!LETS PLAY")
score=0
answer=input("who developed python?")
if answer.lower()=="guide van rossum":
    print("correct answer!")
    score=score+1
else:
    print("incorrect answer")
answer=input("HISTORY OF PYTHON?")
if answer.lower()=="1980":
    print("correct answer!")
    score=score+1
else:
    print("incorrect answer")
answer=input("WHAT CAN PYTHON DO?")
if answer.lower()=="create web applications":
    print("correct answer!")
    score=score+1
else:
    print("incorrect answer")
answer=input("What is python variable?")
if answer.lower()=="Variables are containers for storing data values.":
    print("correct answer!")
    score=score+1
else:
    print("incorrect answer")
answer=input("What is output variable")
if answer.lower()=="The Python print statement is often used to output variables.":
    print("correct answer!")
    score=score+1
else:
    print("incorrect answer")
answer=input("What is python operators?")
if answer.lower()=="Operators are used to perform operations on variables and values.":
    print("correct answer!")
    score=score+1
else:
    print("incorrect answer")
answer=input("What are the different type of operaters in python?")
if answer.lower()=="Arithmetic operators,Assignment operators,Comparison operators,Logical operators,Identity operators":
    print("correct answer!")
    score=score+1
else:
    print("incorrect answer")
answer=input("What is python comments?")
if answer.lower()=="Comments can be used to explain Python code.":
    print("correct answer!")
    score=score+1
else:
    print("incorrect answer")
answer=input("What is IDENTITY OPERATOR")
if answer.lower()=="Identity operators are used to compare the objects":
    print("correct answer!")
    score=score+1
else:
    print("incorrect answer")

print("you got"+str(score)+" qustion correct")
print("you have got :"+str((score/10)*100)+"%")
