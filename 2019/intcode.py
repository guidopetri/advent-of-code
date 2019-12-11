#! /usr/bin/env python3


class Intcode(object):

    def __init__(self, memory=None):
        self.error = False
        self.result = None
        if memory is not None:
            self.set_memory(memory)

    def set_memory(self, memory):
        self.memory = list(memory)
        self.initial_state = list(memory)

    def reset(self):
        self.memory = list(self.initial_state)

    def run(self):
        program_halted = False
        cur_index = 0

        while not program_halted:
            opcode = self.memory[cur_index]

            if opcode == 1:
                operation = self._add
                param_count = 3
            elif opcode == 2:
                operation = self._mul
                param_count = 3
            elif opcode == 99:
                program_halted = True
                continue
            else:
                print('ERROR')
                self.error = True
                return

            # we need to offset by 1 because of the opcode position
            cur_index += 1

            operation(self.memory[cur_index: cur_index + param_count])

            cur_index += param_count

        self.result = self.memory[0]

    def _add(self, params):
        from operator import add

        self.memory[params[2]] = add(self.memory[params[0]],
                                     self.memory[params[1]],
                                     )

    def _mul(self, params):
        from operator import mul

        self.memory[params[2]] = mul(self.memory[params[0]],
                                     self.memory[params[1]],
                                     )

