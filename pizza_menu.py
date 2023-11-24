print("Welcome to pizza deliveries!")
size=(input("What size pizza do you want? S,M or L :"))
pepperonies=(input("Do you want to add pepperonies? yes or no :"))
cheese=input("Do you want to add extra cheese? yes or no : ")
if (size=="S"):
    Bill=15
elif(size=="M"):
    Bill=20
else:
    Bill=25
if(pepperonies=="yes"):
    if(size=="S"):
        Bill+=2
    else:
        Bill+=3
if(cheese=="yes"):
    Bill+=1
print(f"your total bill amount is {Bill}")