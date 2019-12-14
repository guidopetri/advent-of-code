#! /usr/bin/env python3


def read_game(conn_in):
    from collections import defaultdict

    tiles_by_type = defaultdict(list)
    while True:
        if conn_in.poll(2):
            x = conn_in.recv()
            y = conn_in.recv()
            block_type = conn_in.recv()
        else:
            break

        tiles_by_type[block_type].append((x, y))
    print(len(tiles_by_type[2]))
    return


if __name__ == '__main__':
    from multiprocessing import Pipe, Process
    from intcode import Intcode

    with open('13-input.txt', 'r') as f:
        program = f.read().strip()

    program = [int(x) for x in program.split(',')]

    machine_out, arcade_in = Pipe()

    machine = Intcode(program, None, machine_out)

    p_machine = Process(target=machine.run)
    p_arcade = Process(target=read_game, args=(arcade_in,))

    p_machine.start()
    p_arcade.start()

    p_machine.join()
    p_arcade.join()
