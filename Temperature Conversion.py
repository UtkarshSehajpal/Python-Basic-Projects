unit = input("Enter unit of temperature (F / C): ")
temp = float(input("Enter temperature: "))

if unit == "F":
    temp = round((temp - 32) * 5 / 9 ,1)
    print(f"The temperatrue is: {temp} C")

elif unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperatrue is: {temp} F")

else:
    print("*** INVALID INPUT ***")