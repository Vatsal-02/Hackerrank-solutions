import random
user_action = input("Enter a choice (rock, paper, scissors): ")
computer_action = random.choice(possible_actions)


if user_action == computer_action:
    print("Its a tie\nTry Again")

elif user_action == "rock":
    if computer_action == "scissors":
        print("Cheers!!! You win!")
    else:
        print("Sorry You lose\nTry again.")

elif user_action == "paper":
    if computer_action == "rock":
        print("Cheers!!! You win!")
    else:
        print("Sorry You lose\nTry again.")

elif user_action == "scissors":
    if computer_action == "paper":
        print("Cheers!!!You win!")
    else:
        print("Sorry You lose\nTry again.")
