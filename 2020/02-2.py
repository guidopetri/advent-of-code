#! /usr/bin/env python3

import re

with open('02-input.txt', 'r') as f:
    data = f.readlines()

valid_passwords = 0

for line in data:
    match = re.search(r'(\d+)-(\d+) (\w): (\w+)', line)
    lower, upper, letter, password = match.groups()

    lower_idx = int(lower) - 1
    upper_idx = int(upper) - 1

    if (password[lower_idx] == letter) ^ (password[upper_idx] == letter):
        valid_passwords += 1

print(valid_passwords)
