# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:25:01 2023

@author: s24185
"""


def count_neighbours(row, column, table=None):
    if table is None:
        table = [[]]
    rows = len(table)
    cols = len(table[0])
    count = 0
    for t_row in range(max(0, row - 1), min(rows, row + 2)):
        for t_col in range(max(0, column - 1), min(cols, column + 2)):
            if (t_row, t_col) != (row, column) and table[t_row][t_col].get_value == 1:
                count += 1
    return count


def isAlive(row, column, table=None):
    if table is None:
        table = [[]]
    current_alive = (table[row][column] == 1)
    number_of_alive_neighbours = count_neighbours(row, column, table)

    if current_alive and (number_of_alive_neighbours == 2 or number_of_alive_neighbours == 3):
        return 1
    if (not current_alive) and number_of_alive_neighbours == 3:
        return 1
    return 0
