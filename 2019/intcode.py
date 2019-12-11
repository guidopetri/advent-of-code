#! /usr/bin/env python3


class Intcode(object):

    def __init__(self, memory=None):
        self.error = False
        self.result = None
        self.program_halted = True
        if memory is not None:
            self.set_memory(memory)

    def set_memory(self, memory):
        self.memory = list(memory)
        self.initial_state = list(memory)

    def reset(self):
        self.memory = list(self.initial_state)

    def run(self):
        self.program_halted = False
        self.cur_index = 0

        while not self.program_halted:
            opcode = self.memory[self.cur_index] % 100

            if opcode == 1:
                operation = self._add
                param_count = 3
            elif opcode == 2:
                operation = self._mul
                param_count = 3
            elif opcode == 3:
                operation = self._save
                param_count = 1
            elif opcode == 4:
                operation = self._load
                param_count = 1
            elif opcode == 5:
                operation = self._jump_true
                param_count = 2
            elif opcode == 6:
                operation = self._jump_false
                param_count = 2
            elif opcode == 7:
                operation = self._less_than
                param_count = 3
            elif opcode == 8:
                operation = self._equals
                param_count = 3
            elif opcode == 99:
                self.program_halted = True
                continue
            else:
                self.raise_error()

            param_modes = [(self.memory[self.cur_index] // 10 ** (x + 2)) % 10
                           for x in range(param_count)]

            # we need to offset by 1 because of the opcode position
            self.cur_index += 1

            params = self.memory[self.cur_index: self.cur_index + param_count]
            operation(params,
                      param_modes,
                      )

            self.cur_index += param_count

        self.result = self.memory[0]

    def _add(self, params, param_modes):
        assert len(params) == 3
        assert len(param_modes) == 3
        assert param_modes[2] == 0

        from operator import add

        first_op = params[0] if param_modes[0] else self.memory[params[0]]
        second_op = params[1] if param_modes[1] else self.memory[params[1]]

        self.memory[params[2]] = add(first_op,
                                     second_op,
                                     )

    def _mul(self, params, param_modes):
        assert len(params) == 3
        assert len(param_modes) == 3
        assert param_modes[2] == 0

        from operator import mul

        first_op = params[0] if param_modes[0] else self.memory[params[0]]
        second_op = params[1] if param_modes[1] else self.memory[params[1]]

        self.memory[params[2]] = mul(first_op,
                                     second_op,
                                     )

    def _save(self, params, param_modes):
        assert len(params) == 1
        assert len(param_modes) == 1
        assert param_modes[0] == 0

        _in = None
        while not isinstance(_in, int):
            _in = int(input('Add what number to memory? '))

        self.memory[params[0]] = _in

    def _load(self, params, param_modes):
        assert len(params) == 1
        assert len(param_modes) == 1

        _out = params[0] if param_modes[0] else self.memory[params[0]]

        print(_out)

    def _jump_true(self, params, param_modes):
        assert len(params) == 2
        assert len(param_modes) == 2
        assert param_modes[1] == 0

        first = params[0] if param_modes[0] else self.memory[params[0]]
        second = params[1] if param_modes[1] else self.memory[params[1]]

        if first:
            self.cur_index = second

    def _jump_false(self, params, param_modes):
        assert len(params) == 2
        assert len(param_modes) == 2
        assert param_modes[1] == 0

        first = params[0] if param_modes[0] else self.memory[params[0]]
        second = params[1] if param_modes[1] else self.memory[params[1]]

        if first == 0:
            self.cur_index = second

    def _less_than(self, params, param_modes):
        assert len(params) == 3
        assert len(param_modes) == 3
        assert param_modes[2] == 0

        first = params[0] if param_modes[0] else self.memory[params[0]]
        second = params[1] if param_modes[1] else self.memory[params[1]]

        self.memory[params[2]] = int(first < second)

    def _equals(self, params, param_modes):
        assert len(params) == 3
        assert len(param_modes) == 3
        assert param_modes[2] == 0

        first = params[0] if param_modes[0] else self.memory[params[0]]
        second = params[1] if param_modes[1] else self.memory[params[1]]

        self.memory[params[2]] = int(first == second)

    def raise_error(self):
        print('ERROR')
        self.error = True
        self.program_halted = True
