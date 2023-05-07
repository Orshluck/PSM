# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:25:01 2023

@author: s24185
"""

def count_neighbours(row_index, col_index, table):
    rows = len(table)
    cols = len(table[0])
    count = 0
    for r in range(max(0, row_index-1), min(rows, row_index+2)):
        for c in range(max(0, col_index-1), min(cols, col_index+2)):
            if (r, c) != (row_index, col_index) and table[r][c] == 1:
                count += 1
    return count

def isAlive(row,column,table = [[]]):
    current_alive = (table[row][column] == 1)
    number_of_alive_neighbours = count_neighbours(row, column, table)
    
    if current_alive and (number_of_alive_neighbours == 2 or number_of_alive_neighbours == 3):
        return 1
    if (not current_alive )and number_of_alive_neighbours == 3:
        return 1
    return 0