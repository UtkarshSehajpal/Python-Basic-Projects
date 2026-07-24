unit = input("Enter unit (Kg, Pd): ")
mass = float(input("Enter weight: "))

if unit == "Kg":
    weight = mass * 2.205
    print(f"Your weight in Pounds is: {round(weight, 2)}")
elif unit == "Pd":
    weight = mass / 2.205
    print(f"Your weight in Kilograms is: {round(weight, 2)}")

else:
    print("***** INVLAID INPUT *****")
