import random
import time

def spin_row():
    symbols = ["🍋", "🍉", "⭐️", "🔔", "🍒"]
    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    
    return results

def print_row(row):
    print("*" * 12)
    print(" | ".join(row))
    print("*" * 12)

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐️":
            return bet * 20
    else:
        return 0

def main():
    balance = 100

    print()
    print("=" * 60)
    print()
    print("WELCOME TO THE SLOT MACHINE")
    print()
    print("Symbols: 🍋 🍉 ⭐️ 🔔 🍒")
    print()
    print("=" * 60)

    while balance > 0:
        print(f"Current Balance: {balance}")
        print()

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient Funds")
            continue

        elif bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning. . .")
        print()
        time.sleep(2)
        print_row(row)
        print()

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry, you lost this round.")

        balance += payout

        play_again = input("Do you want to spin again? (Y/N): ")
        if play_again!= "Y":
            break
    print()
    print("-----GAME OVER-----")
    print()
    print(f"Your final balance is: ${balance}")
    print()
if __name__ == "__main__":
    main()