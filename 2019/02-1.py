#! /usr/bin/env python3

from operator import add, mul


with open('02-input.txt', 'r') as f:
    codes = [int(x) for x in f.read().split(',')]

# sample input
# codes = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
# codes = [1, 0, 0, 0, 99]
# codes = [2, 3, 0, 3, 99]
# codes = [2, 4, 4, 5, 99, 0]
# codes = [1, 1, 1, 4, 99, 5, 6, 0, 99]

# here we "restore the program to its previous state"
codes[1] = 12
codes[2] = 2

program_halted = False
cur_index = 0

while not program_halted:
    opcode = codes[cur_index]

    if opcode == 1:
        operator = add
    elif opcode == 2:
        operator = mul
    elif opcode == 99:
        program_halted = True
        continue
    else:
        print('ERROR')

    input_1 = codes[cur_index + 1]
    input_2 = codes[cur_index + 2]
    output = codes[cur_index + 3]

    codes[output] = operator(codes[input_1], codes[input_2])

    cur_index += 4

print(codes[0])
