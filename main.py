import random

while True:
    user_action = None
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)

    while user_action not in possible_actions:
        user_action = input("Enter a choice (R, P, S): ").upper()

    if user_action == computer_action:
        print("Player: ", user_action)
        print(+ "Computer: ", computer_action)
        print("It's a Tie")
    elif user_action == "R":
        if computer_action == "P":
            print("Player: ", user_action)
            print("Computer: ", computer_action)
            print("You Lose")
        else:
            print("Player: ", user_action)
            print("Computer: ", computer_action)
            print("You Win")
    elif user_action == "P":
        if computer_action == "R":
            print("Player: ", user_action)
            print("Computer: ", computer_action)
            print("You Win")
        else:
            print("Player: ", user_action)
            print("Computer: ", computer_action)
            print("You Lose")
    elif user_action == "S":
        if computer_action == "R":
            print("Player: ", user_action)
            print("Computer: ", computer_action)
            print("You Lose")
        else:
            print("Player: ", user_action)
            print("Computer: ", computer_action)
            print("You Win")
    play_again = input("Play again? \n (y/n): ")
    if play_again.lower() != "y":
        break
