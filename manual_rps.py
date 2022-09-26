import random 
from enum import IntEnum
# enum helps us to iterate through the sequence, by allowing us to keep track of sequance and the element.
score = 0
class items (IntEnum):
    Rock = 0
    Paper =1
    Scissors =2
# Acquiring computer input
def get_computer_choice():
    choice = random.randint(0, len(items)-1)
    choice_item = items(choice)
    return choice_item
# Acquiring users input
def get_user_choice():
    user_choice = int(input("pick an item: Rock[0], Paper[1] , Scissors[2]"))
    choice_item = items(user_choice)
    return choice_item
# choosing the winner of the game with choices made by the users
def get_winner(computer_choice,user_choice):
    global score

    if computer_choice == user_choice:
        print("It's a tie!")
    elif user_choice == items.Rock:
        if computer_choice == items.Scissors:
            score += 1
            print("Rock eviscerates Scissors, You win!")
        else:
            print("Paper snuffs rock, you Lose!")
    elif user_choice == items.Paper:
        if computer_choice == items.Rock:
            score += 1
            print("Paper snuffs rock, you Win!")
        else:
            print("Scissors shreds Paper, you Lose!")
    elif user_choice == items.Scissors:
        if computer_choice == items.Paper:
            score += 1
            print("Scissors shreds Paper, you Win!")
        else:
            print("Rock destroys Scissors, you Lose")
# Return the score

#function logic
def play():
    while 1 and score !=3:
        try :
            user_choice = get_user_choice()
        except ValueError as e:
            allowed_items = range(0, len(items) - 1)
            print(f"Invalid entry, enter a value from: {allowed_items}")
            continue
        computer_choice = get_computer_choice()
        get_winner(computer_choice, user_choice)

# calling the main
if __name__ == "__main__":
    play()
