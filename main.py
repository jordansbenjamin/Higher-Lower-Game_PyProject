import random
from clear import clear
from game_data import data
from art import logo, vs

# Figure out how to format data from dictionary
def comparison(random, a_or_b):
    '''Grabs data and returns formatted result'''
    # choice = random.choice(data)
    choice = random
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
    score = 0
    winning_choice = None
    while True:
        random.shuffle(data)
        random_a = data.pop()
        random_b = data.pop()
        clear()
        print(logo)

        if score > 0:
            random_a = winning_choice
            print(f"You're right! Current score: {score}")

        a = comparison(random_a, "Compare A")
        print(vs)
        b = comparison(random_b, "Against B")

        higher_count = calculate_count(a, b)
        print(a, b)
        
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()

        if guess == 'A':
            # check_guess(a, score, higher_count)
            guess = a
            if guess == higher_count:
                score += 1
                winning_choice = a
                continue
        elif guess == 'B':
            guess = b
            if guess == higher_count:
                score += 1
                winning_choice = b
                continue
        else:
            break
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        return

game()