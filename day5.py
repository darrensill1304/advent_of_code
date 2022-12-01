import math
import numpy as np


def split_string(string):
    return [char for char in string]


def calculate_bounds(lower, upper, use_lower):
    mid_lower = lower + math.floor((upper - lower) / 2.0)
    mid_upper = mid_lower + 1
    if use_lower:
        return [lower, mid_lower]
    else:
        return [mid_upper, upper]


seat_ids = []
seat_map = np.zeros((128, 8), dtype=bool)
with open('day5-input.txt') as file:
    for line in file:
        inputs = split_string(line.rstrip())
        row_lower = 0
        row_upper = 127
        for ii in range(6):
            row_lower, row_upper = calculate_bounds(row_lower, row_upper, inputs[ii] == "F")
        row = row_lower if inputs[6] == "F" else row_upper

        col_lower = 0
        col_upper = 7
        for jj in range(7, 9):
            col_lower, col_upper = calculate_bounds(col_lower, col_upper, inputs[jj] == "L")
        col = col_lower if inputs[9] == "L" else col_upper

        seat_ids.append(row * 8 + col)
        seat_map[row, col] = True


seat_ids.sort()
print("Max seat ID: {}".format(max(seat_ids)))
for ii in range(len(seat_ids)):
    if seat_ids[ii+1] != seat_ids[ii] + 1:
        print("Your seat ID: {}".format(seat_ids[ii] + 1))
        break
