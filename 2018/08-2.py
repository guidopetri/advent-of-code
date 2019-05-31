#! /usr/bin/env python


class Node():

    def __init__(self, key, parent=None):
        self.parent = parent
        self.total_children = key[0]
        self.total_metadata = key[1]
        self.children = []
        self.metadata = []
        self.value = 0

    def add_child(self, new_child):
        self.children.append(new_child)

    def calculate_value(self):
        if not self.children:
            self.value = sum(self.metadata)
        else:
            for entry in self.metadata:
                if entry == 0:
                    continue
                child_num = entry - 1
                if child_num < len(self.children):
                    self.value += self.children[child_num].value


# read input
with open('08-input.txt', 'r') as f:
    data = f.read().split(' ')

data = [int(x) for x in data]

# header has two numbers exactly: # nodes, # of metadata entries.
# original idea was to use recursion to calculate this, but...
# we hit the max recursion depth and python doesn't support TCO

start = 0
end = 2
root = Node(data[start:end])
last_node = root

while start < len(data):
    start += 2
    if last_node is not None:
        if last_node.total_children == len(last_node.children):
            last_node.metadata = data[start:start + last_node.total_metadata]
            start += last_node.total_metadata

            last_node.calculate_value()
            last_node = last_node.parent
            start -= 2
            continue
    end = start + 2

    if start >= len(data):
        break

    new_node = Node(data[start:end], parent=last_node)
    last_node.add_child(new_node)
    last_node = new_node

print("Root value: {}".format(root.value))
