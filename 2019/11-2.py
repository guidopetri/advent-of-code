#! /usr/bin/env python3


def read_ship(conn_in, conn_out, counter):
    locs = set()

    current_dir = 0
    dirs = [(0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)]

    white_panels = set()
    conn_out.send(1)
    location = (0, 0)

    while True:
        if conn_in.poll(1):
            color = conn_in.recv()
            direction = conn_in.recv()
        else:
            break

        if color:
            white_panels.add(location)
        else:
            white_panels.discard(location)

        if direction:
            current_dir += 1
        else:
            current_dir += 3

        current_dir %= 4
        location = (location[0] + dirs[current_dir][0],
                    location[1] + dirs[current_dir][1],
                    )
        locs.add(location)
        conn_out.send(int(location in white_panels))

    counter.value += len(locs)

    white_panels = list(white_panels)
    max_x = max([x[0] for x in white_panels])
    min_x = min([x[0] for x in white_panels])
    max_y = max([x[1] for x in white_panels])
    min_y = min([x[1] for x in white_panels])

    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x, y) in white_panels:
                print('#', end='')
            else:
                print('.', end='')
        print('\n', end='')
    return


if __name__ == '__main__':
    from multiprocessing import Pipe, Process, Value
    from intcode import Intcode

    with open('11-input.txt', 'r') as f:
        program = f.read().strip()

    program = [int(x) for x in program.split(',')]

    ship_out, robot_in = Pipe()
    robot_out, ship_in = Pipe()

    machine = Intcode(program, robot_in, robot_out)
    counter = Value('i', 0)

    p_robot = Process(target=machine.run)
    p_ship = Process(target=read_ship, args=(ship_in, ship_out, counter))

    p_robot.start()
    p_ship.start()

    p_robot.join()
    p_ship.join()

    print(counter.value)
