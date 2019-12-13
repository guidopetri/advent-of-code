#! /usr/bin/env python3

if __name__ == '__main__':
    from multiprocessing import Pipe, Process, Queue
    from intcode import Intcode
    from itertools import permutations
    # import time

    with open('07-input.txt', 'r') as f:
        program = f.read().strip()

    # sample input
    # program = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'
    # program = '3,23,3,24,1002,24,10,24,1002,23,-1,23,' \
    #           '101,5,23,23,1,24,23,23,4,23,99,0,0'
    # program = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,' \
    #           '1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'
    program = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,' \
              '27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'

    program = [int(x) for x in program.split(',')]

    A_out, B_in = Pipe()
    B_out, C_in = Pipe()
    C_out, D_in = Pipe()
    D_out, E_in = Pipe()
    E_out, A_in = Pipe()

    q = Queue()

    A_machine = Intcode(program, A_in, A_out, 'A', q)
    B_machine = Intcode(program, B_in, B_out, 'B', q)
    C_machine = Intcode(program, C_in, C_out, 'C', q)
    D_machine = Intcode(program, D_in, D_out, 'D', q)
    E_machine = Intcode(program, E_in, E_out, 'E', q)

    machines = [A_machine, B_machine, C_machine, D_machine, E_machine]
    max_output = 0

    for permutation in permutations([5, 6, 7, 8, 9], 5):
        second_input = 0

        processes = []

        for idx, machine in enumerate(machines):
            machine.reset()
            processes.append(Process(target=machine.run))
            if idx == 0:
                machine.set_input([permutation[idx],
                                   second_input])
            else:
                machine.set_input([permutation[idx]])

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        outputs = []

        for idx in range(len(machines)):
            outputs.append(q.get(timeout=5))

        max_output = max(max_output, outputs[-1])

    print(max_output, flush=True)
