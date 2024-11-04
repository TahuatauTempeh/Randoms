import time

print("Welcome to the Number Guesser!")

time.sleep(2)

print("Try to imagine a number between 1 - 10 and we'll try to guess it!")

time.sleep(2)

while True:
    intro_answer_choice_1 = input("Are you ready? (Y/N) ")

    if intro_answer_choice_1 == "Y":

        time.sleep(1)

        print("Let us begin our game! Pick a number between 1 - 10.")

        time.sleep(2)
        
        answer_1 = input("Is your number greater than 5? (Y/N) ")

        if answer_1 == "Y":

            answer_2 = input("Is your number greater than 8? (Y/N) ")

            if answer_2 == "Y":

                answer_3 = input("Is your number 10? (Y/N) ")

                if answer_3 == "Y":

                    print("Your number is 10!")

                else:

                    print("Your number is 9!")

            else:

                answer_3 = input("Is your number 7? (Y/N) ")

                if answer_3 == "Y":

                    print("Your number is 7!")

                else:

                    print("Your number is 8!")

        elif answer_1 == "N":

            answer_2 = input("Is your number less than 3? (Y/N) ")

            if answer_2 == "Y":

                answer_3 = input("Is your number 1? (Y/N) ")

                if answer_3 == "Y":

                    print("Your number is 1!")

                else:

                    print("Your number is 2!")

            else:

                answer_3 = input("Is your number 4? (Y/N) ")

                if answer_3 == "Y":

                    print("Your number is 4!")

                else:

                    print("Your number is 5!")

        else:

            print("Invalid input. Please respond with 'Y' or 'N'.")

        break  

    elif intro_answer_choice_1 == "N":

        time.sleep(1)

        print("Thank you for playing. See you next time!")

        break  

    else:

        time.sleep(1)
        
        print("Invalid input. Please respond with 'Y' or 'N'.")