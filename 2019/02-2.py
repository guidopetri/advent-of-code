#! /usr/bin/env python3

from intcode import Intcode


with open('02-input.txt', 'r') as f:
    program = [int(x) for x in f.read().split(',')]

# sample input
# program = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
# program = [1, 0, 0, 0, 99]
# program = [2, 3, 0, 3, 99]
# program = [2, 4, 4, 5, 99, 0]
# program = [1, 1, 1, 4, 99, 5, 6, 0, 99]

output = None

for noun in range(100):
    for verb in range(100):
        # this is probably a very inefficient way of figuring out
        # the optimal inputs

        program[1] = noun
        program[2] = verb

        machine = Intcode(program)
        machine.run()

        if not machine.error:
            output = machine.result
        else:
            print('There was an error')

        if output == 19690720:
            res_verb = verb
            res_noun = noun
            break
    if output == 19690720:
        break

print('noun: {}, verb: {}, result: {}'.format(res_noun,
                                              res_verb,
                                              100 * res_noun + res_verb))
