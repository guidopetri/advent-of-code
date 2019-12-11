#! /usr/bin/env python3

from intcode import Intcode


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

machine = Intcode(codes)
machine.run()

if not machine.error:
    print(machine.result)
else:
    print('There was an error')
