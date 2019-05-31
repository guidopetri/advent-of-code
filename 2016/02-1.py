#! /usr/bin/env python

with open('02-input.txt', 'r') as f:
    example_data = """ULL
RRDDD
LURDL
UUUUD""".split('\n')  # solution is 1985
    data = f.read().split('\n')

code = []

keypad = [1, 1]

for line in data:
    for character in line:
        if character == 'U':
            keypad[1] -= 1
        elif character == 'D':
            keypad[1] += 1
        elif character == 'L':
            keypad[0] -= 1
        elif character == 'R':
            keypad[0] += 1

        for coord in range(len(keypad)):
            if keypad[coord] > 2:
                keypad[coord] = 2
            if keypad[coord] < 0:
                keypad[coord] = 0

    code.append(keypad[0] + 1 + keypad[1] * 3)

print('Code is: {}'.format(code))
