#! /usr/bin/env python3


class Intcode(object):

    def __init__(self, memory=None, conn_in=None, conn_out=None, id_=None,
                 q=None):
        self.id = id_
        self.q = q
        self.error = False
        self.result = None
        self.program_halted = True
        self.input = None
        self._out = None
        self.conn_in = conn_in
        self.conn_out = conn_out
        self.relative_base = 0
        if memory is not None:
            self.set_memory(memory)

    def set_input(self, input_):
        self.input = input_

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
            elif opcode == 9:
                operation = self._set_relative
                param_count = 1
            elif opcode == 99:
                self.program_halted = True
                continue
            else:
                self.raise_error()
                continue

            param_modes = [(self.memory[self.cur_index] // 10 ** (x + 2)) % 10
                           for x in range(param_count)]

            self.old_index = self.cur_index

            params = self.memory[self.cur_index + 1:
                                 self.cur_index + 1 + param_count]
            operation(params,
                      param_modes,
                      )

            if self.old_index == self.cur_index:
                # we need to offset by 1 because of the opcode position
                self.cur_index += 1
                self.cur_index += param_count

        self.result = self.memory[0]

        # if self.conn_in is not None:
        #     self.conn_in.close()
        # if self.conn_out is not None:
        #     self.conn_out.close()

        if self.q is not None:
            self.q.put(self._out)

    def _resolve_param(self, param, mode):
        if mode == 2:
            return self._get_at_mem(param, True)
        elif mode == 1:
            return param
        elif mode == 0:
            return self._get_at_mem(param, False)

    def _add(self, params, param_modes):
        assert len(params) == 3
        assert len(param_modes) == 3
        assert param_modes[2] in (0, 2)

        from operator import add

        first = self._resolve_param(params[0], param_modes[0])
        second = self._resolve_param(params[1], param_modes[1])

        self._set_at_mem(params[2],
                         param_modes[2] == 2,
                         add(first,
                             second,
                             ))

    def _mul(self, params, param_modes):
        assert len(params) == 3
        assert len(param_modes) == 3
        assert param_modes[2] in (0, 2)

        from operator import mul

        first = self._resolve_param(params[0], param_modes[0])
        second = self._resolve_param(params[1], param_modes[1])

        self._set_at_mem(params[2],
                         param_modes[2] == 2,
                         mul(first,
                             second,
                             ))

    def _save(self, params, param_modes):
        assert len(params) == 1
        assert len(param_modes) == 1
        assert param_modes[0] in (0, 2)

        _in = None

        if self.input is not None and self.input:
            _in = self.input.pop(0)

        elif self.conn_in is not None:
            _in = self.conn_in.recv()

        while not isinstance(_in, int):
            _in = int(input('Add what number to memory? '))

        self._set_at_mem(params[0],
                         param_modes[0] == 2,
                         _in)

    def _load(self, params, param_modes):
        assert len(params) == 1
        assert len(param_modes) == 1
        self._out = self._resolve_param(params[0], param_modes[0])

        if self.conn_out is not None:
            self.conn_out.send(self._out)
        else:
            print(self._out)

    def _jump_true(self, params, param_modes):
        assert len(params) == 2
        assert len(param_modes) == 2

        first = self._resolve_param(params[0], param_modes[0])
        second = self._resolve_param(params[1], param_modes[1])

        if first:
            self.cur_index = second

    def _jump_false(self, params, param_modes):
        assert len(params) == 2
        assert len(param_modes) == 2

        first = self._resolve_param(params[0], param_modes[0])
        second = self._resolve_param(params[1], param_modes[1])

        if first == 0:
            self.cur_index = second

    def _less_than(self, params, param_modes):
        assert len(params) == 3
        assert len(param_modes) == 3
        assert param_modes[2] in (0, 2)

        first = self._resolve_param(params[0], param_modes[0])
        second = self._resolve_param(params[1], param_modes[1])

        self._set_at_mem(params[2],
                         param_modes[2] == 2,
                         int(first < second))

    def _equals(self, params, param_modes):
        assert len(params) == 3
        assert len(param_modes) == 3
        assert param_modes[2] in (0, 2)

        first = self._resolve_param(params[0], param_modes[0])
        second = self._resolve_param(params[1], param_modes[1])

        self._set_at_mem(params[2],
                         param_modes[2] == 2,
                         int(first == second))

    def _set_relative(self, params, param_modes):
        assert len(params) == 1
        assert len(param_modes) == 1

        change = self._resolve_param(params[0], param_modes[0])

        self.relative_base += change

    def _get_at_mem(self, loc, relative):
        if relative:
            base = self.relative_base
        else:
            base = 0

        self._check_mem(loc + base)
        return self.memory[loc + base]

    def _set_at_mem(self, loc, relative, value):
        if relative:
            base = self.relative_base
        else:
            base = 0

        self._check_mem(loc + base)
        self.memory[loc + base] = value

    def _check_mem(self, loc):
        if len(self.memory) <= loc:
            self.memory.extend([0 for _ in range(loc - len(self.memory) + 1)])

    def raise_error(self):
        print('ERROR')
        self.error = True
        self.program_halted = True
