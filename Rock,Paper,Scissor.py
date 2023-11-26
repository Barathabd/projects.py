Rock=''' _    
               | |   
 _ __ ___   ___| | __
| '__/ _ \ / __| |/ /
| | | (_) | (__|   < 
|_|  \___/ \___|_|\_\
                     
                     '''
Paper='''_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|        '''

Scissor='''         _                        
         (_)                       
 ___  ___ _ ___ ___  ___  _ __ ___ 
/ __|/ __| / __/ __|/ _ \| '__/ __|
\__ \ (__| \__ \__ \ (_) | |  \__ \
|___/\___|_|___/___/\___/|_|  |___/'''
import random
print("Welcome to rock,paper,scissor game!")
list=[Rock,Paper,Scissor]
Decision=int(input("What do you want to choose? type 0 for rock,1 for paper,2 for scissor:"))
choice=list[Decision]
print("your choice is :",choice)
A=random.randint(0,2)
computer_choice=list[A]
print("Computer's choice is",computer_choice)
if (choice==computer_choice):
    print("Game is draw.")
elif (choice==list[0]and computer_choice==list[2]):
    print("You Win")
elif(choice==list[1] and computer_choice==list[0]):
    print("You Win")
elif(choice==list[2] and computer_choice==list[1]):
    print("You Win")
else:
    print("You Loose")
    


