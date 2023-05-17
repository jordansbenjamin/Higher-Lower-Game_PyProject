import random
from game_data import data
from art import logo, vs

# Figure out how to format data from dictionary
def comparison(a_or_b):
    '''Grabs data and returns formatted result'''
    choice = random.choice(data)
    name = choice['name']
    # f_count = choice['follower_count']
    desc = choice['description']
    country = choice['country']
    print(f"{a_or_b}: {name}, a {desc}, from {country}.")

def game():
    '''Main game function that handles all the games logic'''
    print(logo)
    comparison("Compare A")
    print(vs)
    comparison("Against B")

game()