#! /usr/bin/env python


class Room(object):

    def __init__(self, name, sector_id, checksum):
        self.name = name
        self.sector_id = sector_id
        self.checksum = checksum

    @property
    def decoy(self):
        name_no_hyphen = self.name.replace('-', '')
        char_counts = [(i, self.name.count(i)) for i in set(name_no_hyphen)]
        # in order to sort by reverse on x[1], but normal on x[0]...
        # i divide 1 by x[1] so that i can sort both normally :)
        char_counts.sort(key=lambda x: (1/x[1], x[0]))
        print(char_counts)
        return self.checksum != ''.join([x[0] for x in char_counts[:5]])

    def real_name(self):
        rotation = self.sector_id % 26
        clean_name = self.name.replace('-', ' ')
        rotated_name = []
        for char in clean_name:
            if char == ' ':
                rotated_char = ' '
            else:
                # normalize to 1-26, then convert back to ascii index
                rotated_char = chr((ord(char) + rotation - 97) % 26 + 97)
            rotated_name.append(rotated_char)

        return ''.join(rotated_name)

    def __repr__(self):
        return "Room: {}, {}, {}".format(self.name,
                                         self.sector_id,
                                         self.checksum)


with open('04-input.txt', 'r') as f:
    data = f.read()

example = 'qzmt-zixmtkozy-ivhz-343[zimth]'

rooms = []

for line in data.split('\n'):
    first_split = line.split('[')
    checksum = first_split[1][:-1]
    second_split = first_split[0].split('-')
    sector_id = int(second_split[-1])
    name = '-'.join(second_split[:-1])

    rooms.append(Room(name, sector_id, checksum))

print([room.sector_id for room in rooms if 'orth' in room.real_name()])
