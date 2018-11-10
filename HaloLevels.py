# write a dictionary for all halo levels
# add a function to pull out a random value and shift the other ones down
# just make it a list and have it remove a level

import numpy
levels = []
length = len(levels)
skulls = ["Iron", "Black Eye", "Tough Luck", "Catch", "Cloud", "Famine", "Thunderstorm", "Tilt", "Mythic", "Blind", "Cowbell", "Grunt Birthday", "IWHBYD"]
class Skull:
    def __init__(self, name="", mult=1.0, secondary=False):
        self.name = name
        self.mult = mult
        self.secondary = secondary
    

def choose(A):
    x = numpy.random.randint(0, len(A))
    del A[x]
    return x

def level_select():
    for i in range(length):
        x = numpy.random.randint(0, len(levels))
        print("Time to play " + str(levels[x]))
        del levels[x]
        answer = ""
        while answer != "Y":
            answer = input("Ready for next level? (Y): ")
        print("\n\n")


def add_skull(current_diff, diff_cap):
    return  
    

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
