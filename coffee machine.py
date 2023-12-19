MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def enough_resources(order_ingredients):
    for i in order_ingredients:
        if order_ingredients[i]>=resources[i]:
            print("Sorry there is no enough {i}")
            return False
    return True
    
    
    
    
    
    
def coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def make_drink(user_wish,drink_ingredients):
    for z in drink_ingredients:
        resources[z]-=drink_ingredients[z]
    print  (f"Here is your drink {user_wish}☕️,enjoy!")  
    




is_on=True
while is_on:
    user_wish=input("What would you like to drink?(espresso/cappuccino/latte): ").lower()
    if user_wish=="off":
        is_on=False
    elif user_wish=="report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
    else:
        drink=MENU[user_wish]
        if enough_resources(drink["ingredients"]):
            payment=coins()
            if payment<drink["cost"]:
                print("sorry , There is no enough money")
            elif payment>drink["cost"]:
                change=round(payment-drink["cost"],2)
                print(f"Here is your change ${change}")
                make_drink(user_wish,drink["ingredients"])
                
                
        