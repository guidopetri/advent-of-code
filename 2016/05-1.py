#! /usr/bin/env python

from hashlib import md5


with open('05-input.txt', 'r') as f:
    data = f.read()

example = 'abc'
solution = []
index = 0

while len(solution) < 8:
    to_hash = data + str(index)
    in_bytes = bytes(to_hash, encoding='utf-8')
    hashed = md5(in_bytes).hexdigest()
    if hashed.startswith('00000'):
        print(hashed)
        solution.append(hashed[5])

    index += 1

print('solution: {}'.format(''.join(solution)))
