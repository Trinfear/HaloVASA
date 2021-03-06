# write a dictionary for all halo levels
# add a function to pull out a random value and shift the other ones down
# just make it a list and have it remove a level

import numpy as np
import pandas as pd
'''
class Skull:
    def __init__(self, name="", mult=1.0, game="Reach", secondary=False):
        self.name = name
        self.mult = mult
        self.game = game
        self.secondary = secondary
'''
'''
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
'''
'''
def choose(a):
    x = np.random.randint(0, len(a))
    del a[x]
    return x
'''
'''
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
'''
'''
def add_skull(current_diff, diff_cap):
    return  
'''
'''
def fill_levels(levels):
    for i in range(15):
        levels.append('Halo 2: level ' + str(i))
        levels.append('Halo 5: ' + str(i))

    for i in range(10):
        levels.append('Halo 1: level ' + str(i))
        levels.append('Halo 3: level ' + str(i))
        levels.append('Reach: level ' + str(i))
        levels.append('Halo 4: level ' + str(i))
'''
'''
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
'''
'''
def choose_halo_difficulty():
    diff = np.random.choice(['Legendary', 'Heroic', 'Normal', 'Easy'])
    return diff, difficulties[diff]
'''

# Read all options from file
opts = {}
for line in open("options.txt", "r"):
    # Check if line is comment/blank
    if(line[0] == '#' or len(line) <= 1):
        continue
    line = line.rstrip('\n')
    line = line.split(' = ')
    # Convert numeric options to integers
    if(line[1].isnumeric()):
        line[1] = int(line[1])
    opts[line[0]] = line[1]
#for v in opts: print(v, "\t"*(3-int(len(v)/8)), '=',  opts[v]) # DEBUG

# Read skulls and level data
skulls = pd.read_csv(opts['skullfile'], skiprows=0)
levels = pd.read_csv(opts['levelfile'], skiprows=0)
# Hardcoded halo difficulty multiplier dictionary
halo_diff_dict = {'Legendary': 4, 'Heroic': 2, 'Normal': 1, 'Easy': 0.25}
#print(skulls.head()) # DEBUG

# Set base difficulty
diff = opts['default_difficulty']
if(opts['prompt_difficulty']):
    diff = int(input("Enter a difficulty value: "))

# Choose level
#print('\n', levels, '\n') # DEBUG
# Extract valid halo games from options
possible_games = opts['valid_games'].split(', ')
if(possible_games == "Any"):
    possible_games = ['Halo 1', 'Halo 2', 'Halo 3', 'Halo 3 ODST', 'Reach', 'Halo 4', 'Halo 5']
#print(levels) # DEBUG
possible_levels = levels.loc[ 
                                (levels['Cutscene Level'] == 0) & 
                                (levels['Game'].isin(possible_games))
                            ]

# Choose halo difficulty
valid_halo_diffs = opts['valid_halo_difficulties'].split(', ')
chosen_halo_diff = np.random.choice(valid_halo_diffs)

#print(possible_levels, '\n') # DEBUG
level = possible_levels.sample(1)
#print(level, '\n') # DEBUG

# Get possible skulls/modifiers for selected level
# Skulls
chosen_game = level['Game'].to_string(index=False)
possible_skulls = skulls.loc[ 
                                (skulls[chosen_game] == 1)
                            ]
#print(possible_skulls, '\n') # DEBUG
                            


# Modify multiplier until we done
current_diff = 10
# Use spreadsheet difficulty instead of default if option set
if(opts['use_level_multiplier']):
    current_diff = int(level['Multiplier'])
# Apply halo difficulty multiplier
current_diff *= halo_diff_dict[chosen_halo_diff]

chosen_skulls = []
while(current_diff < diff):
    #print("Current Difficulty:", current_diff) # DEBUG
    chosen_skulls.append(possible_skulls.sample(1, replace=False))
    possible_skulls.drop(chosen_skulls[-1].index, inplace=True)
    #print('\n', chosen_skulls[-1], '\n') # DEBUG
    mult = float((chosen_skulls[-1]['Multiplier'].to_string(index=False)))
    current_diff *= mult
    #print("Current Difficulty:", current_diff) # DEBUG
    if(len(possible_skulls) == 0):
        print("Out of skulls!")
        break
    
print('{} ({}) on {}'.format(level['Name'].to_string(index=False), chosen_game, chosen_halo_diff))
print('SKULLS:')
for skull in chosen_skulls:
    print('\t', skull['Name'].to_string(index=False))
print('\nGoal Difficulty:', diff)
print('Goal Difficulty:', round(current_diff))

#print(levels)
#level_select()
'''
print(skulls[0].name)
print(skulls[0].mult)
print(skulls[0].secondary)
print(skulls[0].game)
'''