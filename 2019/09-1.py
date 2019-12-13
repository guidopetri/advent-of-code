#! /usr/bin/env python3

from intcode import Intcode


with open('09-input.txt', 'r') as f:
    program = [int(x) for x in f.read().split(',')]

# sample input
# program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
# program = [104, 1125899906842624, 99]
# program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101,
#            0, 99]

machine = Intcode(program)
machine.run()
