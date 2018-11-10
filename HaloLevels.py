# write a dictionary for all halo levels
# add a function to pull out a random value and shift the other ones down
# just make it a list and have it remove a level

import numpy
levels = []
length = len(levels)
difficulties = {'Legendary': 4, 'Heroic': 2, 'Normal': 1, 'Easy': 0.25}


def level_select():
    for i in range(length):
        x = numpy.random.randint(0, len(levels))
        print("Time to play " + levels[x])
        del levels[x]
        answer = ""
        while answer != "Y":
            answer = input("Ready for next level? (Y): ")
        select_difficulty()
        print("\n\n")

# Dumb ass merging test


def fill_levels():
    for i in range(15):
        levels.append('Halo 2: level ' + str(i))
        levels.append('Halo 5: ' + str(i))

    for i in range(10):
        levels.append('Halo 1: level ' + str(i))
        levels.append('Halo 3: level ' + str(i))
        levels.append('Reach: level ' + str(i))
        levels.append('Halo 4: level ' + str(i))

    levels.sort()


def select_difficulty():
    # call other functions to get difficulty
    challanges = []
    difficulty = 0
    difficulty_min = 18
    difficulty_max = 25
    new_challanges, new_diffulty = choose_difficulty()
    challanges.append(new_challanges)
    difficulty += new_diffulty
    new_challanges, new_diffulty = add_skull(difficulty_min, difficulty_max, difficulty)
    print(challanges, difficulty)


def choose_difficulty():
    diff = numpy.random.choice('Legendary', 'Heroic', 'Normal', 'Easy')
    return diff, difficulties[diff]


fill_levels()
level_select()
