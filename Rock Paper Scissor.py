import random

options = ("rock" , "paper" , "scissor")
player = None

computer = random.choice(options)
running = True

while running:
    player = input("Enter your choice (rock / paper / scissor): ")

    while player not in options:
        print("Your input is not an option!")
        print("Please try again.")
        player = input("Enter your choice (rock / paper / scissor): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Its a tie!")
    else:
        if player == "rock" and computer == "paper":
            print("Computer Wins!")
        elif player == "rock" and computer == "scissor":
            print("Player Wins!")
        elif player == "paper" and computer == "rock":
            print("Player Wins!")
        elif player == "paper" and computer == "scissor":
            print("Computer Wins!")
        elif player == "scissor" and computer == "paper":
            print("Player Wins")
        elif player == "scissor" and computer == "rock":
            print("Computer Wins!")
    
    play = input("Do you want to play again (Y/N): ")
    if play == "Y":
        running = True
    else:
        running = False

print()
print("Thanks for Playing!")