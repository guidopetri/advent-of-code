#! /usr/bin/env python3


def calc_seat_id(seat):
    seat = seat.strip()

    def binary_split(seat_range, partition):
        midway_point = len(seat_range) // 2
        if partition in 'RB':
            return seat_range[midway_point:]
        else:
            return seat_range[:midway_point]

    seat_range = list(range(128))
    for partition in seat[:7]:
        seat_range = binary_split(seat_range, partition)
    row = seat_range[0]

    seat_range = list(range(8))
    for partition in seat[7:]:
        seat_range = binary_split(seat_range, partition)
    col = seat_range[0]

    seat_id = row * 8 + col
    return seat_id


with open('05-input.txt', 'r') as f:
    data = f.readlines()

seat_ids = list(map(calc_seat_id, data))
print(max(seat_ids))
