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
    if a > b:
        return a
    return b

def calculate_count(a, b):
    '''Checks higher follower count'''
    return a if a > b else b

def game():
    '''Main game function that handles all the games logic'''
    while True:
        print(logo)
        a = comparison("Compare A")
        print(vs)
        b = comparison("Against B")

        higher_count = calculate_count(a, b)
        
        user_guess = input("Who has more followers? Type 'A' or 'B': ")

        if user_guess == 

        




game()