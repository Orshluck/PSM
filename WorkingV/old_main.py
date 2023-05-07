
import pygame
from old_game_of_life import *
from old_Board import *
import time
import random

# Initialize pygame
pygame.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def color_is():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    return (r, g, b)


# Set the dimensions of each square
SQUARE_SIZE = 10
# Set the number of squares in each row and column
n = 75

WINDOW_SIZE = (n * SQUARE_SIZE, n * SQUARE_SIZE)

# Table of Tables
table = [[0 for j in range(n)] for i in range(n)]
temporary_table = [[0 for j in range(n)] for i in range(n)]
clicked_squares = []

def draw_square(screen, row, col, color):
    x = col * SQUARE_SIZE
    y = row * SQUARE_SIZE
    pygame.draw.rect(screen, color, [x, y, SQUARE_SIZE, SQUARE_SIZE])


def draw_screen(screen, table):
    for row in range(len(table)):
        for column in range(len(table)):
            value = table[row][column]
            if value == 1:
                color = BLACK
            else:
                color = WHITE
            draw_square(screen, row, column, color)


def calculate_new_state(table, temp_table):
    for row in range(len(table)):
        for column in range(len(table)):
            value = isAlive(row, column, table)
            temp_table[row][column] = value


def copyTable(tableToCopy, tablefromCopy):
    for row in range(len(tableToCopy)):
        for column in range(len(tableToCopy)):
            tableToCopy[row][column] = tablefromCopy[row][column]


# Create the pygame window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Fill the background with white
screen.fill(WHITE)

font = pygame.font.Font(None, 36)
restart_button = pygame.Rect(10, 10, 100, 50)
restart_text = font.render("PAUSE", True, BLACK)

# Run the game loop
running = True


# generate both boards


def start_game():
    global clicked_squares
    generate_starting_set(table)
    copyTable(temporary_table, table)
    draw_screen(screen, table)
    clicked_squares = []

def check_if_dead():
    for row in range(len(table)):
        for column in range(len(table)):
            if table[row][column] == 1:
                return True
    return False


start_game()
pause = False;
while running:
    if not pause:
        calculate_new_state(table, temporary_table)
        draw_screen(screen, temporary_table)

        copyTable(table, temporary_table)
        pygame.draw.rect(screen, WHITE, restart_button)

    screen.blit(restart_text, (restart_button.x + 10, restart_button.y + 10))

    pygame.display.flip()
    time.sleep(0.3)
    if not check_if_dead():
        time.sleep(1)
        start_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if restart_button.collidepoint(pos):
                pause = not pause
                print("mommy")

# Quit pygame
pygame.quit()
