foods = []
prices = []
total = 0

food = input("Enter your food item or Q to quit: ")
food.lower()

while food != "q":
    foods.append(food)

    price = float(input("Enter price of your food item: "))
    total += price
    prices.append(price)

    food = input("Enter your food item or Q to quit: ")
print()
print()

print("=" * 50)
print("You Shopping Cart (Food : Price)--> ")
print()

for i in range(len(foods)):
    print(f"{foods[i]} : {prices[i]}")

print("-" * 20)
print("Total is:" ,total)
print("-" * 20)
print()
