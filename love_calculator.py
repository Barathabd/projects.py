print("Welcome to the love calculator!")
Name1=str(input("What is your name?\n"))
Name2=str(input("What is their name?\n"))
Two_names=Name1+Name2
Lower_case=Two_names.lower()
t=Lower_case.count("t")
r=Lower_case.count("r")
u=Lower_case.count("u")
e=Lower_case.count("e")
True_score=t+r+u+e

l=Lower_case.count("l")
o=Lower_case.count("o")
v=Lower_case.count("v")
e=Lower_case.count("e")
Love_score=l+o+v+e
Total_score=int(str(True_score)+str(Love_score))

if((Total_score<10) or (Total_score>90)):
    print(f"your score is {Total_score}, you go together like coke and mentos")
elif((Total_score>=40) and (Total_score<=50)):
    print(f"your score is {Total_score}, you are alright together")
else:
    print(f"your score is{Total_score} ")