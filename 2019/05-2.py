#! /usr/bin/env python3

from intcode import Intcode


with open('05-input.txt', 'r') as f:
    program = [int(x) for x in f.read().split(',')]

# sample input
program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
           1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
           999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]

machine = Intcode(program)
machine.run()
