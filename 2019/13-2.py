#! /usr/bin/env python3


def read_game(conn_in, conn_out):
    import pygame

    pygame.display.init()
    pygame.font.init()

    play_surface = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont('Arial', 16)
    empty = font.render(' ', True, pygame.Color(255, 255, 255))
    wall = font.render('x', True, pygame.Color(255, 255, 255))
    block = font.render('#', True, pygame.Color(255, 255, 255))
    paddle = font.render('_', True, pygame.Color(255, 255, 255))
    ball = font.render('@', True, pygame.Color(255, 255, 255))

    tiles = {0: empty,
             1: wall,
             2: block,
             3: paddle,
             4: ball,
             }

    actuals = {}
    gathering_info = True

    while True:
        while gathering_info:
            if conn_in.poll(1):
                x = conn_in.recv()
                y = conn_in.recv()
                block_type = conn_in.recv()
            else:
                gathering_info = False

            if (x, y) == (-1, 0):
                print('Current score: {}'.format(block_type), flush=True)
                continue

            actuals[(x * 16, y * 16)] = block_type

            if block_type == 4:
                current_ball_pos = (x, y)
                print('ball: {}'.format(current_ball_pos), flush=True)

            if block_type == 3:
                current_paddle_pos = (x, y)
                print('paddle: {}'.format(current_paddle_pos), flush=True)
        else:
            gathering_info = True

            play_surface.fill(pygame.Color(0, 0, 0))
            for loc, tile in actuals.items():
                play_surface.blit(tiles[tile], loc)

            pygame.display.flip()

            if current_paddle_pos[0] > (current_ball_pos[0] + 1):
                _out = -1
            elif current_paddle_pos[0] == (current_ball_pos[0] + 1):
                _out = 0
            elif current_paddle_pos[0] < (current_ball_pos[0] + 1):
                _out = 1
            conn_out.send(_out)
            print('sent {}'.format(_out), flush=True)
            continue
        break

    print('exited main loop', flush=True)

    pygame.quit()

    return


if __name__ == '__main__':
    from multiprocessing import Pipe, Process
    from intcode import Intcode
    import pygame

    pygame.display.init()
    pygame.font.init()

    with open('13-input.txt', 'r') as f:
        program = f.read().strip()

    program = [int(x) for x in program.split(',')]
    program[0] = 2

    machine_out, arcade_in = Pipe()
    machine_in, arcade_out = Pipe()

    machine = Intcode(program, machine_in, machine_out)

    p_machine = Process(target=machine.run)
    p_arcade = Process(target=read_game, args=(arcade_in, arcade_out))

    p_machine.start()
    p_arcade.start()

    p_machine.join()
    p_arcade.join()
