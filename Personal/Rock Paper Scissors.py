import time
import random
while True :
    print("Let's play Rock! Paper! Scissors! ")
    time.sleep(1)
    print("Let's play! ")
    time.sleep(1)
    action_1 = input("Enter your choice Rock, Paper, Scissor : ")
    time.sleep(1)
    possible_actions = ["Rock","Paper","Scissor"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {action_1}, computer chose {computer_action}.\n")
    time.sleep(1)
    if action_1 == computer_action:
        print(f"Both players selected {action_1}. It's a tie!")
    elif action_1 == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif action_1 == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif action_1 == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    time.sleep(1)
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break