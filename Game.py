import time

from main import *

start_game()

while running:
    calculate_new_state(screen, table)
    actualize_table(table)
    draw_screen(screen,table)
    set_new_state(table)
    pygame.display.flip()
    time.sleep(1)
    if not check_if_dead():
        #time.sleep(3)
        start_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit pygame
pygame.quit()
