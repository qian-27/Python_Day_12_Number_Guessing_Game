from art import logo
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_answer(guess_num, right_num, turns):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess_num > right_num:
        print(f"Too high.")
        return turns - 1
    elif guess_num < right_num:
        print(f"Too low.")
        return turns - 1
    else:
        print(f"You got it! The number was {right_num}")

# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Main function
def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    right_num = randint(1,100)
    # print(f"The right number is {right_num}")

    turns = set_difficulty()

    while turns > 0:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess_num = int(input("Make a guess: "))
        turns = check_answer(guess_num, right_num, turns)
        if guess_num == right_num:
            return
        elif turns == 0:
            print("You've run out of guesses, you lose.")

# Call the function
game()
