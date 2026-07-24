principle = float(input("Enter your Principal balance: "))
while principle < 0:
    print("Principal cannot be negative!")
    principle = float(input("Enter your Principal balance again: "))

rate = float(input("Enter your interest rate: "))
while rate < 0:
    print("Rate cannot be negative")
    rate = float(input("Enter your interest rate again: "))

time = float(input("Enter your time: "))
while time < 0:
    print("Time cannot be negative")
    time = float(input("Enter your Time again: "))


amt = principle * ((1 + rate / 100) ** time)
print(f"Your final amount will be ${amt:.2f}")