import random

print("ROCK PAPER SCISSORS")

while True:
    user_input = input("Enter R for rock, S for scissors, P for paper, or Q to quit: ").upper()
    computer_input = random.choice(["R", "S", "P"])
    print("Computer chooses:", computer_input)

    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "R" and computer_input == "S") or \
         (user_input == "S" and computer_input == "P") or \
         (user_input == "P" and computer_input == "R"):
        print("You win!")
    elif (user_input == "R" and computer_input == "P") or \
         (user_input == "S" and computer_input == "R") or \
         (user_input == "P" and computer_input == "S"):
        print("You lose!")

    if user_input == "Q":
        print("Thank you for playing!")
        break
    elif user_input not in ["R", "S", "P", "Q"]:
        print("Invalid input. Please try again.")
