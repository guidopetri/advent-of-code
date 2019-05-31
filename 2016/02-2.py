#! /usr/bin/env python


def get_code_number(keypad):  # how inefficient
    if keypad[1] == -2:
        return '1'
    elif keypad[1] == 2:
        return 'D'
    elif keypad[0] == -2:
        return '5'
    elif keypad[0] == 2:
        return '9'
    elif keypad == [-1, -1]:
        return '2'
    elif keypad == [-1, 0]:
        return '6'
    elif keypad == [-1, 1]:
        return 'A'
    elif keypad == [0, -1]:
        return '3'
    elif keypad == [0, 0]:
        return '7'
    elif keypad == [0, 1]:
        return 'B'
    elif keypad == [1, -1]:
        return '4'
    elif keypad == [1, 0]:
        return '8'
    elif keypad == [1, 1]:
        return 'C'


with open('02-input.txt', 'r') as f:
    example_data = """ULL
RRDDD
LURDL
UUUUD""".split('\n')  # solution is 5DB3
    data = f.read().split('\n')

code = []

keypad = [-2, 0]

for line in data:
    for character in line:
        if character == 'U':
            keypad[1] -= 1
            if sum(map(abs, keypad)) > 2:
                keypad[1] += 1
        elif character == 'D':
            keypad[1] += 1
            if sum(map(abs, keypad)) > 2:
                keypad[1] -= 1
        elif character == 'L':
            keypad[0] -= 1
            if sum(map(abs, keypad)) > 2:
                keypad[0] += 1
        elif character == 'R':
            keypad[0] += 1
            if sum(map(abs, keypad)) > 2:
                keypad[0] -= 1

    number = get_code_number(keypad)
    code.append(number)

print('Code is: {}'.format(code))
