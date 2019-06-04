#! /usr/bin/env python


class Room(object):

    def __init__(self, name, sector_id, checksum):
        self.name = name
        self.sector_id = sector_id
        self.checksum = checksum

    def verify_checksum(self):
        char_counts = [(i, self.name.count(i)) for i in set(self.name)]
        # in order to sort by reverse on x[1], but normal on x[0]...
        # i divide 1 by x[1] so that i can sort both normally :)
        char_counts.sort(key=lambda x: (1/x[1], x[0]))
        return self.checksum == ''.join([x[0] for x in char_counts[:5]])

    def __repr__(self):
        return "Room: {}, {}, {}".format(self.name,
                                         self.sector_id,
                                         self.checksum)


with open('04-input.txt', 'r') as f:
    data = f.read()

example = 'not-a-real-room-404[oarel]'

rooms = []

for line in data.split('\n'):
    first_split = line.split('[')
    checksum = first_split[1][:-1]
    second_split = first_split[0].split('-')
    sector_id = int(second_split[-1])
    name = ''.join(second_split[:-1])

    rooms.append(Room(name, sector_id, checksum))

print(sum(room.sector_id for room in rooms if room.verify_checksum()))
