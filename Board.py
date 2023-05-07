import random

from Box import Box


def generate_starting_set(table=None, ):
    if table is None:
        table = [[]]
    # up and down
    for row in range(len(table)):
        for column in range(len(table)):
            randomvalue = random.randrange(0, 10)
            if randomvalue < 7:
                temp_box = Box(0)
            else:
                temp_box = Box(1)
            table[row][column] = temp_box

    return table
