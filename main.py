import Board

import pygame
import game_of_life
import time
import random

# Initialize pygame
from Box import Box

pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the dimensions of each square
SQUARE_SIZE = 10
# Set the number of squares in each row and column
n = 50

WINDOW_SIZE = (n * SQUARE_SIZE, n * SQUARE_SIZE)
table = []

for column in range(n):
    table.append([])
    for row in range(n):
        table[column].append(Box(0))


def draw_square(screen, row, col, color):
    x = col * SQUARE_SIZE
    y = row * SQUARE_SIZE
    pygame.draw.rect(screen, color, [x, y, SQUARE_SIZE, SQUARE_SIZE])

def getColorAge(age):
    # Convert the input value to a percentage between 0 and 100
    percentage = int(age * 100 / 255)

    # Calculate the red and green values based on the percentage
    red = int(0+age/20)
    green = int(255-age/20)

    # Return the color as a tuple of (red, green, blue)
    #return BLACK
    return (red, green, 0)

def draw_screen(screen, table):
    for row in range(len(table)):
        for column in range(len(table)):
            box = table[row][column]
            value = box.get_value()
            age = box.get_age()
            if value == 1:
                color = getColorAge(age)

            else:
                color = WHITE
            draw_square(screen, row, column, color)


def calculate_new_state(screen, table):
    for row in range(len(table)):
        for column in range(len(table)):
            value = game_of_life.isAlive(row, column, table)
            table[row][column].set_t_value(value)

def set_new_state(table):
    for row in range(len(table)):
        for column in range(len(table)):
            table[row][column].correct_value()

def copyTable(tableToCopy, tablefromCopy):
    for row in range(len(tableToCopy)):
        for column in range(len(tableToCopy)):
            tableToCopy[row][column] = tablefromCopy[row][column]


# Create the pygame window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Fill the background with white
screen.fill(WHITE)

# Run the game loop
running = True

def start_game():
    Board.generate_starting_set(table)
    draw_screen(screen, table)
def check_if_dead():
    for row in range(len(table)):
        for column in range(len(table)):
            if table[row][column].get_value() == 1:
                return True
    return False

def actualize_table(table):
    for row in range(len(table)):
        for column in range(len(table)):
            if table[row][column].get_temporary_value == 1:
                table[row][column].grow_old()


##################################################################
###                 Game starts here                        ######

