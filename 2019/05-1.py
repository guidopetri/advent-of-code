#! /usr/bin/env python3

from intcode import Intcode


with open('05-input.txt', 'r') as f:
    program = [int(x) for x in f.read().split(',')]

machine = Intcode(program)
machine.run()
