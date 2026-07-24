questions = (
    ("How many elements are there in the Perodic table?: "),
    ("How many planets are there in the solar system?: "),
    ("Which animal lays the largest egg?: "),
    ("What element is commonly used in Nuclear Power Plants?: ")
)

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. 6", "B. 7", "C. 8", "D. 9"),
            ("A. Monkey", "B. Ostrich", "C. Bhalu", "D. Leon"),
            ("A. Oxygen", "B. Uranium", "C. Carbon", "D. Techinium"))

answers = ("C", "C", "B", "B")
guesses = []
score = 0
question_number = 0

print()
print()
for question in questions:
    print()
    print("-" * 60)
    print(question)
    for option in options[question_number]:
        print()
        print(option)
    print()

    guess = input("Enter your option (A / B / C / D): ").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer!")
        print(f"{answers[question_number]} is the correct answer")

    question_number += 1

print("=" * 50)
print()
print(f"Your final score is: {score / len(questions) * 100}%")
print("Thank you :)")
print()
print("=" * 50)