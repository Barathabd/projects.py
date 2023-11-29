import random 
print("Welcome to the password generator!")
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','_,','+']
Number_of_letters=int(input("How many letters would you like in your password? \n"))
Number_of_numbers=int(input("How many numbers would you like to have in your password? \n"))
Number_of_symbols=int(input("How many symbols would you like to have in your password? \n"))
password_list=[]
for i in range(1,Number_of_letters+1):
    password_list.append(random.choice(letters))
for i in range(1,Number_of_numbers+1):
    password_list.append(random.choice(numbers))
for i in range(1,Number_of_symbols+1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(f"Here is your new password : {password}")