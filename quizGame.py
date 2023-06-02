#Python mini project on quiz game
import random
print("\nWelcome to a python quiz!\n")
print("You get +1 for correct answer\n-1 for a wrong answer.\nDon't forget to check your scores later!")
score=0
QnA=[
    ["Are strings immutable in python?","True","False",1],
    ["Which operator has higher precedence?","exponent","paranthesis",2],
    ["Can we use the \'else\' block for \' for\' loop?", "No","Yes",2],
    ["Guess the output:\nfro i in range(10,15,1):\n\tprint(i,end=\'\')","10 11 12 13 14 ","10 11 12 13 14 15 ",1],
    ["\'in\' operator is used to check whether the element is present in the iterable object or not:","True","False",1],
    ["What is the output of the following:\np,q,r=10,11,12\nprint(p,q,r)","10 11 12","Error:Invlid Syntax",1],
    ["What is the output of the following code?\nstrg=\"python\"\nprint(strg[1:3])","yth","pyt",1],
    ["What is the output of the following code?\nlistOne = [20, 40, 60, 80]\nlistTwo = [20, 40, 60, 80]\n\nprint(listOne == listTwo)\nprint(listOne is listTwo)","True\nTrue","False\nTrue",2],
    ["What is the output of the following code?\nvar= \"James Bond\"\nprint(var[2::-1])","dno","maJ",2],
    ["What is the output of the following code?\nvalueOne = 5 ** 2\nvalueOne = 5 ** 3\n\nprint(valueOne)\nprint(valueTwo)","10\n15","25\n125",2]

]
for i in range(0,5):
    Q=random.choice(QnA)
    print("Question ",i,":")
    print(Q[0],"\n")
    print(f"1.{Q[1]}   2.{Q[2]}")
    A=int(input("Enter answer:"))
    if A==Q[3]:
        print("\ncorrect answer\n")
        score=score+1
        print("Score:",score)
    if A!=Q[3]:
       print("\nwrong answer\n")
       score=score-1
       print("Score:",score)

print("Final results:\n")
print(score)
