#! /usr/bin/env python


class Marble():

    def __init__(self, value):
        self.value = value
        self.next_clockwise = None
        self.previous_clockwise = None

    def set_between(self, prev_marble, next_marble):
        self.next_clockwise = next_marble
        self.previous_clockwise = prev_marble
        next_marble.previous_clockwise = self
        prev_marble.next_clockwise = self

    def get_previous(self):
        return self.previous_clockwise

    def get_next(self):
        return self.next_clockwise

    def __repr__(self):
        return "Next marble: {}, " \
               "Previous marble: {}, " \
               "Value: {}".format(self.next_clockwise.value,
                                  self.previous_clockwise.value,
                                  self.value)


class CircularQueue():

    def __init__(self, starting_marble):
        self.head = starting_marble
        starting_marble.next_clockwise = starting_marble
        starting_marble.previous_clockwise = starting_marble

    def insert_marble(self, new_marble):
        next_marble = self.head.get_next().get_next()
        prev_marble = self.head.get_next()
        new_marble.set_between(prev_marble, next_marble)
        self.head = new_marble

    def current_marble(self):
        return self.head

    def pop_7_behind(self):
        marble_to_pop = self.current_marble()
        for x in range(7):
            marble_to_pop = marble_to_pop.get_previous()
        prev_marble = marble_to_pop.get_previous()  # 18
        next_marble = marble_to_pop.get_next()  # 19
        next_marble.set_between(prev_marble, next_marble.get_next())
        self.head = next_marble

        return marble_to_pop

    def __repr__(self):
        queue = [self.head.value]
        current = self.head.get_next()
        while current != self.head:
            queue.append(current.value)
            current = current.get_next()
        queue.append(self.head.value)

        return queue.__repr__()


class Player():

    counter = 0

    def __init__(self):
        Player.counter += 1
        self.score = 0
        self.id = Player.counter

    def add_marble(self, marble):
        self.score += marble.value

    def get_score(self):
        return self.score


def marble_game_logic(players, last_marble_value):

    circle = CircularQueue(Marble(0))

    for value in range(1, last_marble_value + 1):

        current_player = players[(value - 1) % PLAYER_COUNT]

        new_marble = Marble(value)

        if value % 23 == 0:
            other_marble = circle.pop_7_behind()
            current_player.add_marble(new_marble)
            current_player.add_marble(other_marble)
        else:
            circle.insert_marble(new_marble)

    return circle


# 428 players; last marble is worth 70825 points
with open('09-input.txt', 'r') as f:
    content = f.read().split()

# this is yet another new data structure: the circular queue

content = [int(x) for x in content if x.isdigit()]

PLAYER_COUNT = content[0]
LAST_MARBLE_VALUE = content[1] * 100

# other examples:

# 32
# PLAYER_COUNT = 9
# LAST_MARBLE_VALUE = 25

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
# PLAYER_COUNT = 30
# LAST_MARBLE_VALUE = 5807

players = []
for player in range(1, PLAYER_COUNT + 1):
    players.append(Player())

circle = marble_game_logic(players, LAST_MARBLE_VALUE)

scores = {player.get_score(): player.id for player in players}

best_score = max(scores.keys())
best_scorer = scores[best_score]

print("Best score was {} by player {}".format(best_score, best_scorer))
