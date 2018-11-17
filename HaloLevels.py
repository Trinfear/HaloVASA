# write a dictionary for all halo levels
# add a function to pull out a random value and shift the other ones down
# just make it a list and have it remove a level

import numpy as np
import pandas as pd

class Skull:
    def __init__(self, name="", mult=1.0, game="Reach", secondary=False):
        self.name = name
        self.mult = mult
        self.game = game
        self.secondary = secondary


def generate_skull_list():
    skulls = [Skull("Iron", 1.0),
              Skull("Black Eye", 1.0),
              Skull("Tough Luck", 1.0),
              Skull("Catch", 1.0),
              Skull("Cloud", 1.0),
              Skull("Famine", 1.0),
              Skull("Thunderstorm", 1.0),
              Skull("Tilt", 1.0),
              Skull("Mythic", 1.0),
              Skull("Blind", 1.0, True),
              Skull("Cowbell", 1.0, True),
              Skull("Grunt Birthday", 1.0, True), 
              Skull("EDITIWHBYD", 1.0, True),
            ]
    return skulls


def choose(a):
    x = np.random.randint(0, len(a))
    del a[x]
    return x


def level_select():
    for i in range(length):
        x = np.random.randint(0, len(levels))
        print("Time to play " + levels[x])
        del levels[x]
        answer = ""
        while answer != "Y":
            answer = input("Ready for next level? (Y): ")
        select_difficulty()
        print("\n\n")


def add_skull(current_diff, diff_cap):
    return  


def fill_levels(levels):
    for i in range(15):
        levels.append('Halo 2: level ' + str(i))
        levels.append('Halo 5: ' + str(i))

    for i in range(10):
        levels.append('Halo 1: level ' + str(i))
        levels.append('Halo 3: level ' + str(i))
        levels.append('Reach: level ' + str(i))
        levels.append('Halo 4: level ' + str(i))


def select_difficulty():
    # call other functions to get difficulty
    challenges = []
    difficulty = 0
    difficulty_min = 18
    difficulty_max = 25
    new_challenges, new_difficulty = choose_halo_difficulty()
    challaeges.append(new_challenges)
    difficulty += new_difficulty
    new_challenges, new_difficulty = add_skull(difficulty_min, difficulty_max, difficulty)
    challaeges.append(new_challenges)
    difficulty += new_difficulty
    print(challanges, difficulty)


def choose_halo_difficulty():
    diff = np.random.choice(['Legendary', 'Heroic', 'Normal', 'Easy'])
    return diff, difficulties[diff]

# Read all options from file
opts = {}
for line in open("options.txt", "r"):
    line = line.rstrip('\n')
    line = line.split(' = ')
    opts[line[0]] = line[1]
print(opts) # DEBUG

skulls = pd.read_csv(opts['skullfile'], skiprows=0)
levels = pd.read_csv(opts['levelfile'], skiprows=0)
print(skulls.head()) # DEBUG

difficulties = {'Legendary': 4, 'Heroic': 2, 'Normal': 1, 'Easy': 0.25}


#print(levels)
#level_select()
'''
print(skulls[0].name)
print(skulls[0].mult)
print(skulls[0].secondary)
print(skulls[0].game)
'''