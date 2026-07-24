
def show_balance(balance):
    print(f"Your Balance is: {balance:.2f}")

def deposit():
    amount = float(input("Enter an amout to deposit: "))
    if amount < 0:
        print("Invalid Amount!")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))

    if amount > balance:
        print("Insufficient Funds!")
        return 0
    
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    
    else:
        return amount

def main():
    balance = 0
    is_running = True
    print()
    print()
    print("=" * 60)
    print()

    print("Welcome to the Bank of Niggora!")
    print()

    while is_running:
        print("Choose your action-")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_balance(balance)
            print()

        elif choice == 2:
            balance += deposit()
            print()

        elif choice == 3:
            balance -= withdraw(balance)
            print()

        elif choice == 4:
            is_running = False
            print()
            print("Visit us again!")
            print()

        else:
            print("*" * 60)
            print()
            print("INVALID INPUT!")
            print()
            print("*" * 60)
            print()


if __name__ == "__main__":
    main()