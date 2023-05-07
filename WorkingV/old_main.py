
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

info = pygame.display.Info()
height = info.current_h

# Print the height
print(height)
# Set the dimensions of each square
SQUARE_SIZE = 15
# Set the number of squares in each row and column
n = 48

WINDOW_SIZE = (n * SQUARE_SIZE, n * SQUARE_SIZE)
pygame.display.set_caption("Conway Game Of Life")
# Table of Tables
table = [[0 for j in range(n)] for i in range(n)]
temporary_table = [[0 for j in range(n)] for i in range(n)]
save_table =[[0 for j in range(n)] for i in range(n)]

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
            # draw lines between squares
            pygame.draw.line(screen, (200, 200, 200), (column * SQUARE_SIZE, row * SQUARE_SIZE),
                             ((column + 1) * SQUARE_SIZE, row * SQUARE_SIZE), 1)
            pygame.draw.line(screen, (200, 200, 200), (column * SQUARE_SIZE, row * SQUARE_SIZE),
                             (column * SQUARE_SIZE, (row + 1) * SQUARE_SIZE), 1)


def calculate_new_state(table, temp_table):
    for row in range(len(table)):
        for column in range(len(table)):
            value = isAlive(row, column, table)
            temp_table[row][column] = value


def copyTable(tableToCopy, tablefromCopy):
    for row in range(len(tableToCopy)):
        for column in range(len(tableToCopy)):
            tableToCopy[row][column] = tablefromCopy[row][column]



copyTable(save_table,table)

# Create the pygame window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Fill the background with white
screen.fill(WHITE)

font = pygame.font.Font(None, 36)
pause_button = pygame.Rect(10, 10, 100, 50)
pause_text = font.render("START", True, BLACK)

restart_button = pygame.Rect(120, 10, 120, 50)
restart_button_text = font.render("RESTART", True, BLACK)

random_button = pygame.Rect(260, 10, 120, 50)
random_text = font.render("RANDOM", True, BLACK)


save_button = pygame.Rect(400, 10, 120, 50)
save_text = font.render("SAVE", True, BLACK)

reload_button = pygame.Rect(540, 10, 120, 50)
reload_text = font.render("RELOAD", True, BLACK)
# Run the game loop
running = True


# generate both boards


def start_game():
    generate_starting_set(table)
    copyTable(temporary_table, table)
    draw_screen(screen, table)


def check_if_dead():
    for row in range(len(table)):
        for column in range(len(table)):
            if table[row][column] == 1:
                return True
    return False

pause = True
start_game()
while running:
    if not pause:
        calculate_new_state(table, temporary_table)
        draw_screen(screen, temporary_table)
        copyTable(table, temporary_table)

    pygame.draw.rect(screen, WHITE, pause_button)
    screen.blit(pause_text, (pause_button.x + 10, pause_button.y + 10))

    pygame.draw.rect(screen, WHITE, restart_button)
    screen.blit(restart_button_text, (restart_button.x + 10, restart_button.y + 10))

    pygame.draw.rect(screen, WHITE, random_button)
    screen.blit(random_text, (random_button.x + 10, random_button.y + 10))

    pygame.draw.rect(screen, WHITE, save_button)
    screen.blit(save_text, (save_button.x + 10, save_button.y + 10))

    pygame.draw.rect(screen, WHITE, reload_button)
    screen.blit(reload_text, (reload_button.x + 10, restart_button.y + 10))

    pygame.display.flip()
    if  pause:
        time.sleep(0)
    else:
        time.sleep(0.1)
    if not check_if_dead():
        time.sleep(1)
        start_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            row = int(event.pos[1]/SQUARE_SIZE)
            column = int(event.pos[0]/SQUARE_SIZE)
            if table[row][column] == 1:
                table[row][column] = 0
                temporary_table[row][column] = 0
                draw_square(screen, row, column, (255, 0, 0))

            else:
                table[row][column] = 1
                temporary_table[row][column] = 1
                draw_square(screen, row, column, (0, 255, 0))

            pygame.display.flip()


        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if pause_button.collidepoint(pos):
                print("yes")
                pause = not pause
                if pause:
                    pause_text = font.render("START", True, BLACK)
                else:
                    pause_text = font.render("PAUSE", True, BLACK)
            if restart_button.collidepoint(pos):
                start_game()
                pause = True
                pause_text = font.render("START", True, BLACK)
            if random_button.collidepoint(pos):
                start_game()
                table = generate_random_board(table)
                pause = False
                pause_text = font.render("PAUSE", True, BLACK)
            if save_button.collidepoint(pos):
                copyTable(save_table,table)
            if reload_button.collidepoint(pos):
                print("hi")
                table = save_table
                temporary_table = save_table
                draw_screen(screen,table)
                pygame.display.flip()

# Quit pygame
pygame.quit()
