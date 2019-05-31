#! /usr/bin/env python


class Tree():

    def __init__(self, key):
        self.processed = False
        self.key = key
        self.current_depth = 0
        self.current_index = 2
        self.children_list = [self.key[0]]
        self.metadata_list = [self.key[1]]
        self.metadata_sum = 0

    def walk(self):
        if self.children_list[-1] > 0:
            self.current_depth += 1
            self.children_list.append(self.key[self.current_index])
            self.current_index += 1
            self.metadata_list.append(self.key[self.current_index])
        elif self.children_list[-1] == 0:
            if self.metadata_list[-1] > 0:
                print("adding %s to metadata" % self.key[self.current_index])
                self.metadata_sum += self.key[self.current_index]
                self.metadata_list[-1] -= 1
            if self.metadata_list[-1] == 0:
                self.current_depth -= 1
                del self.children_list[-1]
                del self.metadata_list[-1]
                if len(self.children_list) > 0:
                    self.children_list[-1] -= 1
        self.current_index += 1

        if self.current_index >= len(self.key):
            self.processed = True


# read input
with open('08-input.txt', 'r') as f:
    content = f.read().split()

content = [int(x) for x in content]

# header has two numbers exactly: # nodes, # of metadata entries.
# original idea was to use recursion to calculate this, but...
# we hit the max recursion depth and python doesn't support TCO

tree = Tree(content)

while not tree.processed:
    tree.walk()

print("final metadata sum: %s" % tree.metadata_sum)
