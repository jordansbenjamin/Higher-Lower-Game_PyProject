import random
from game_data import data
from art import logo, vs

# Figure out how to format data from dictionary
def comparison(a_or_b):
    '''Grabs data and returns formatted result'''
    choice = random.choice(data)
    name = choice['name']
    f_count = choice['follower_count']
    desc = choice['description']
    country = choice['country']
    print(f"{a_or_b}: {name}, a {desc}, from {country}.")
    return f_count


def calculate_count(a, b):
    '''Checks higher follower count'''
    return a if a > b else b

# def check_guess(a_or_b, score, higher_count):
#     guess = a_or_b
#     if guess == higher_count:
#         score += 1
#         winning_choice = a_or_b

def game():
    '''Main game function that handles all the games logic and flow'''
    while True:
        score = 0
        winning_choice = None
        print(logo)

        if score > 0:
            a = winning_choice
            print(f"You're right! Current score: {score}")

        a = comparison("Compare A")
        print(vs)
        b = comparison("Against B")

        higher_count = calculate_count(a, b)
        
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if guess == 'A':
            check_guess(a, score, higher_count)
            continue
        elif guess == 'B':
            check_guess(b, score, higher_count)
            continue
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return

# Figure out scoring when user guesses the correct answer, needs to print at the top under the logo
# Else the game ends and reveal their score anyways

game()