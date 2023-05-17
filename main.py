import random
from game_data import data

# Figure out how to format data from dictionary
def comparison(a_or_b):
    '''Grabs data and returns formatted result'''
    choice = random.choice(data)
    name = choice['name']
    f_count = choice['follower_count']
    desc = choice['description']
    country = choice['country']
    return f"{a_or_b}: {name}, a {desc}, from {country}."

print(comparison("Compare A"))
print(comparison("Against B"))
