# write a dictionary for all halo levels
# add a function to pull out a random value and shift the other ones down
# just make it a list and have it remove a level

import numpy
levels = []
length = len(levels)
for i in range(length):
    x = numpy.random.randint(0, len(levels))
    print("Time to play " + str(levels[x]))
    del levels[x]
    answer = ""
    while answer != "Y":
        answer = input("Ready for next level? (Y): ")
    print("\n\n")

x = 0
while x < 0:
    pass
