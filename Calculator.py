print()

print("=" * 50)
print("Welcome to your Calulator!  :)")
operator = input("Enter your operator (+, -, *, /): ")
num1 = float(input("Enter First number: "))
num2 = float(input("Enter Second number: "))
print("=" * 50)
print()

if operator == "+":
    print(f"The sum is: {num1 + num2}")
elif operator == "-":
    print(f"Subtration is: {num1 - num2}")
elif operator == "*":
    print(f"The multiplication is: {num1 * num2}")
elif operator == "/":
    print(f"The Division is: {num1 / num2}")
else:
    print("INVALID INPUT!")
print()

print("END!")
print("*" * 50)