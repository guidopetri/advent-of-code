#! /usr/bin/env python

import re


# read input
with open('05-input.txt', 'r') as f:
    content = f.read()

re_string = re.compile(r'(\w)(\1)', flags=re.IGNORECASE)
position = 0

results = {}

for letter in 'abcdefghijklmnopqrstuvwxyz':
    trimmed_content = re.sub(letter, r'', content, flags=re.IGNORECASE)

    while re_string.search(trimmed_content, position) is not None:
        match = re_string.search(trimmed_content, position)
        if match.group(1) != match.group(2):
            trimmed_content = (trimmed_content[:match.start(1)]
                               + trimmed_content[match.end(2):])
            position = 0
        else:
            position = match.end(1)
    results[letter] = len(trimmed_content)

print(min(results.items(), key=lambda x: x[1]))
