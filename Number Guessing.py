import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print()
print("=" * 50)
print("---Welcome to the Number Guessing Game!---")
print()
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("Guess is out of number range!")
        elif guess < answer:
            print("Too low. Try a higher number")
        elif guess > answer:
            print("Too high. Try a lower number")
        else:
            print("*" * 40)
            print()    
            print(f"YOU GOT IT! The number is {answer}")
            print(f"Number of guesses: {guesses}")
            print()
            print("*" * 40)
            is_running = False

    else:
        print("INVALID INPUT! Has to be a number.")