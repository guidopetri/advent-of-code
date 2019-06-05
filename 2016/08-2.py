#! /usr/bin/env python

import re


def transpose(screen):
    return list(map(list, zip(*screen)))


def execute_command(command, screen):
    if command.startswith('rect '):
        y_size, x_size = map(int, re.findall(r'\d+', command))
        for x in range(x_size):
            for y in range(y_size):
                screen[x][y] = '#'
    elif command.startswith('rotate row'):
        row_num, amount = map(int, re.findall(r'\d+', command))
        screen[row_num] = screen[row_num][-amount:] + screen[row_num][:-amount]
    elif command.startswith('rotate column'):
        col_num, amount = map(int, re.findall(r'\d+', command))
        screen = transpose(screen)
        screen[col_num] = screen[col_num][-amount:] + screen[col_num][:-amount]
        screen = transpose(screen)
    return screen


with open('08-input.txt', 'r') as f:
    data = f.read().split('\n')

example = """rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1""".split('\n')

screen = [['.' for x in range(50)] for y in range(6)]

for line in data:
    screen = execute_command(line, screen)

screen = transpose(screen)

for i in range(0, len(screen), 5):
    transposed = transpose(screen[i:i+5])
    print('\n'.join([''.join(x) for x in transposed]))
    print('\n')
