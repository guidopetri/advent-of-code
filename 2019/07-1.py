#! /usr/bin/env python3

from intcode import Intcode
from itertools import permutations


with open('07-input.txt', 'r') as f:
    program = f.read().strip()

# sample input
# program = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
# program = '3,23,3,24,1002,24,10,24,1002,23,-1,23,' \
#           '101,5,23,23,1,24,23,23,4,23,99,0,0'
# program = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,' \
#           '1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'

program = [int(x) for x in program.split(',')]

A_machine = Intcode(program)
B_machine = Intcode(program)
C_machine = Intcode(program)
D_machine = Intcode(program)
E_machine = Intcode(program)

machines = [A_machine, B_machine, C_machine, D_machine, E_machine]
max_output = 0

for permutation in permutations([0, 1, 2, 3, 4], 5):
    second_input = 0

    for idx, machine in enumerate(machines):
        machine.reset()
        machine.set_input((x for x in [permutation[idx], second_input]))
        machine.run()
        second_input = machine._out

    max_output = max(max_output, second_input)

print(max_output)
