# write a dictionary for all halo levels
# add a function to pull out a random value and shift the other ones down
# just make it a list and have it remove a level

import numpy
levels = []
length = len(levels)


def level_select():
    for i in range(length):
        x = numpy.random.randint(0, len(levels))
        print("Time to play " + str(levels[x]))
        del levels[x]
        answer = ""
        while answer != "Y":
            answer = input("Ready for next level? (Y): ")
        print("\n\n")

# Dumbass merging test

def fill_levels():
    for i in range(15):
        levels.append('H2: ' + str(i))
        levels.append('H5: ' + str(i))

    for i in range(10):
        levels.append('H1: ' + str(i))
        levels.append('H3: ' + str(i))
        levels.append('HR: ' + str(i))
        levels.append('H4: ' + str(i))

    levels.sort()


def select_difficulty():
    x = 0
    while x < 0:
        pass
