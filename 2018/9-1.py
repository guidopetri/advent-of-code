#! /usr/bin/env python


class Marble():

    def __init__(self, value):
        self.value = value
        self.next_clockwise = None
        self.previous_clockwise = None

    def set_next(self, prev_marble):
        self.next_clockwise = prev_marble.next_clockwise
        self.previous_clockwise = prev_marble
        self.next_clockwise.previous_clockwise = self
        self.previous_clockwise.next_clockwise = self

    def __repr__(self):
        return "Next marble: {}, " \
               "Previous marble: {}, " \
               "Value: {}".format(self.next_clockwise.value,
                                  self.previous_clockwise.value,
                                  self.value)


def marble_game_logic(players, last_marble_value):
    value = 0
    marbles = []
    while value <= last_marble_value:

        new_marble = Marble(value)
        if value == 0:
            new_marble.next_clockwise = new_marble
            new_marble.previous_clockwise = new_marble
        # elif value == 23:
        #     new_marble.set_next(marbles[-7])
        else:
            new_marble.set_next(marbles[-1])
        marbles.append(new_marble)
        # print([marble.value for marble in marbles])
        value += 1
    return marbles[-1]


# 428 players; last marble is worth 70825 points
with open('9-input.txt', 'r') as f:
    content = f.read().split()

content = [int(x) for x in content if x.isdigit()]

# PLAYER_COUNT = content[0]
# LAST_MARBLE_VALUE = content[1]

# other examples:

# 32
PLAYER_COUNT = 9
LAST_MARBLE_VALUE = 25

# 8317
# PLAYER_COUNT = 10
# LAST_MARBLE_VALUE = 1618

# 146373
# PLAYER_COUNT = 13
# LAST_MARBLE_VALUE = 7999

# 2764
# PLAYER_COUNT = 17
# LAST_MARBLE_VALUE = 1104

# 54718
# PLAYER_COUNT = 21
# LAST_MARBLE_VALUE = 6111

# 37305
# PLAYER_COUNT = 21
# LAST_MARBLE_VALUE = 5807

print(marble_game_logic(PLAYER_COUNT, LAST_MARBLE_VALUE))
