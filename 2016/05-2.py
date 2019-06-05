#! /usr/bin/env python

from hashlib import md5


def get_printable(solution, last, all_red=False):
    joined = []
    if all_red:
        joined.append(RED)
    for x in range(len(solution)):
        if solution[x] is not None:
            if last == x:
                joined.append(RED)
                joined.append(solution[x])
                if not all_red:
                    joined.append(NC)
            else:
                joined.append(solution[x])
        else:
            joined.append(' ')
    joined.append(NC)
    return ''.join(joined)


with open('05-input.txt', 'r') as f:
    data = f.read()

example = 'abc'
solution = [None for x in range(8)]
index = 0
RED = '\033[0;31m'
NC = '\033[0m'
last_digit = 0

while None in solution:
    to_hash = data + str(index)
    in_bytes = bytes(to_hash, encoding='utf-8')
    hashed = md5(in_bytes).hexdigest()
    print(get_printable(solution, last_digit), end='    ')
    print(hashed, end='\r')
    if hashed.startswith('00000'):
        if hashed[5] in (str(x) for x in range(8)):
            position = int(hashed[5])
            character = hashed[6]
            if solution[position] is None:
                solution[position] = character
                last_digit = position

    index += 1

print(get_printable(solution, last_digit, True), end='    ')
print(hashed, end='\r')
