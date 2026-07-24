
#----Setting the Menu----
menu = {"Popcorn" : 6.0,                
        "Pizza" : 3.0,
        "Nachos" : 4.5,
        "Fries" : 2.5,
        "Chips" : 1.0,
        "Pretzel" : 3.5,
        "Soda" : 3.0,
        "Lemonade" : 4.25}

#----Creating Variables----
cart = []                               
total = 0



#----Displaying Menu----
print("=" * 40)                         
print() 

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:<10} : ${value:<10,.2f}")

print()
print("=" * 40)



#----Taking User Input----
food = input("Select an item (Q to quit): ").capitalize()        

while food != "Q":
    if menu.get(food) is not None:
        cart.append(food)
        food = input("Select an item (Q to quit): ").capitalize()
    else:
        print("Item not in menu!")
        food = input("Select an item (Q to quit): ").capitalize()
print()
print()



#----Displaying Cart----
print("Your cart is: ")
num = 1
for food in cart:
    print(f"{num}. {food}")
    num += 1



#----Totaling the Bill----
for food in cart:
    total += menu.get(food)
print()
print()

print("*" * 30)
print()
print(f"Total : ${total:.2f}")
print()
print("*" * 30)