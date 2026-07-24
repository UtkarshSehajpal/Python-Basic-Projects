"""
1. Username is no more than 12 characters
2. Username must not contain spaces
3. Username must not contain digits
"""

name = input("Enter your name: ")

if len(name) > 12:
    print("Too long name!")
elif not name.isalpha():
    print("Name cannot have spaces or digits!")
else:
    print("Your name is:" , name)