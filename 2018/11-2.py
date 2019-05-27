#! /usr/bin/env python

import pandas as pd


with open('11-input.txt', 'r') as f:
    grid_serial_number = f.read()

grid_serial_number = int(grid_serial_number)

# start the power level process here
grid_as_list = [[(y + 1) * (x + 11) for y in range(300)] for x in range(300)]

fuel_cells = pd.DataFrame(grid_as_list)

# let's not use .apply()
for column in fuel_cells.columns:
    # add serial number
    fuel_cells[column] = fuel_cells[column] + grid_serial_number
    # times (X coordinate + 10) which is index + 11
    fuel_cells[column] = fuel_cells[column] * (fuel_cells.index + 11)

    # keep hundreds digit
    fuel_cells[column] = fuel_cells[column] // 100  # divide by 100, truncate
    fuel_cells[column] = fuel_cells[column] % 10

    # subtract 5
    fuel_cells[column] = fuel_cells[column] - 5

# original idea was to aggregate neighboring columns then neighboring rows
# but using .rolling().sum() is better
last_max_power = 0
ideal_grid_size = 1
grid_x = 0
grid_y = 0

for i in range(1, 301):
    power_grid = fuel_cells.rolling(i, center=True, axis=0).sum()
    power_grid = power_grid.rolling(i, center=True, axis=1).sum()
    power_grid = power_grid.astype(float)

    max_power = power_grid.max().max()
    if max_power > last_max_power:
        ideal_grid_size = i
        last_max_power = max_power
        grid_x = power_grid.max(axis=1).idxmax() - (i // 2) + 1
        grid_y = power_grid.max(axis=0).idxmax() - (i // 2) + 1

print("Best X: {}".format(grid_x))
print("Best Y: {}".format(grid_y))
print("Best grid size: {}".format(ideal_grid_size))
print("Max total power: {}".format(last_max_power))
