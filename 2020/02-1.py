#! /usr/bin/env python3

import re

with open('02-input.txt', 'r') as f:
    data = f.readlines()

valid_passwords = 0

for line in data:
    match = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
    lower_lim, upper_lim, letter, password = match.groups()

    count = password.count(letter)

    if int(lower_lim) <= count and count <= int(upper_lim):
        valid_passwords += 1

print(valid_passwords)
