#! /usr/bin/env python3

if __name__ == '__main__':
    from multiprocessing import Pipe, Process, Queue
    from intcode import Intcode
    from itertools import permutations

    with open('07-input.txt', 'r') as f:
        program = f.read().strip()

    # sample input
    # program = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,'\
    #           '1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,'\
    #           '2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'
    # program = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,' \
    #           '27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'

    program = [int(x) for x in program.split(',')]

    q = Queue()

    max_output = 0

    for permutation in permutations([5, 6, 7, 8, 9], 5):
        A_out, B_in = Pipe()
        B_out, C_in = Pipe()
        C_out, D_in = Pipe()
        D_out, E_in = Pipe()
        E_out, A_in = Pipe()

        A_machine = Intcode(program, A_in, A_out, 'A', q)
        B_machine = Intcode(program, B_in, B_out, 'B', q)
        C_machine = Intcode(program, C_in, C_out, 'C', q)
        D_machine = Intcode(program, D_in, D_out, 'D', q)
        E_machine = Intcode(program, E_in, E_out, 'E', q)

        machines = [A_machine, B_machine, C_machine, D_machine, E_machine]
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

        if max_output < outputs[-1]:
            max_output = outputs[-1]
            max_perm = permutation

    print(max_output, max_perm, flush=True)
