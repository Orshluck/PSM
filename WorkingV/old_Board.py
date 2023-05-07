import random

def generate_starting_set(table=None,):
    if table is None:
        table = [[]]
    #up and down
    for row in range(len(table)):
        for column in range(len(table)):
            randomshit = random.randrange(0,10)
            if randomshit < 12:
                value = 0
            else:
                value = 1
            table[row][column] = value
           
    return table

def generate_random_board(table = None):
    if table is None:
        table = [[]]
    # up and down
    for row in range(len(table)):
        for column in range(len(table)):
            randomshit = random.randrange(0, 10)
            if randomshit < 6:
                value = 0
            else:
                value = 1
            table[row][column] = value

    return table
