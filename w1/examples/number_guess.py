import random


def within_range(number, min=None, max=None):
    """
    Given a possible minimum and maximum, return True if the number is between
    the min and max, otherwise return False.
    """
    if min is not None and number < min:
        return False
    if max is not None and number > max:
        return False
    return True

print("Peter was here")

def play_game(min, max):
    unused_variable = 1
    print_instructions()
    number_to_guess = random.randint(min, max)
    number_guessed = False
    guesses = 0

    while not number_guessed and guesses < 10:
        guess = input_integer("What's your guess? ", min=1, max=1000)
        guesses += 1
        if guess == number_to_guess:
            print("You got it right!")
            number_guessed = True
        elif guess < number_to_guess:
            print("Too low!")
        else:
            print("Too high!")


def print_instructions():
    print(
        "I am going to choose a number between 1 and 1000. You have 10 guesses to get it right."
    )


def input_integer(prompt, min=None, max=None):
    """
    Ask the user for an integer within a range. If invalid input given,
    keep asking until you get valid input.
    """
    guess = input(prompt)
    while not (is_integer(guess) and within_range(int(guess), min, max)):
        print("Invalid input")
        guess = input(prompt)
    return int(guess)


def is_integer(string):
    return string.isdigit()


def within_range(number, min=None, max=None):
    """
    Given a possible minimum and maximum, return True if the number is between
    the min and max, otherwise return False.
    """
    if min is not None and number < min:
        return False
    if max is not None and number > max:
        return False
    return True


min = 1
max = 1000
play_game(min, max)
