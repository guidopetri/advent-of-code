#! /usr/bin/env python

import re


# read input
with open('5-input.txt', 'r') as f:
    content = f.read()

re_string = re.compile(r'(\w)(\1)', flags=re.IGNORECASE)
position = 0

while re_string.search(content, position) is not None:
    match = re_string.search(content, position)
    if match.group(1) != match.group(2):
        content = content[:match.start(1)] + content[match.end(2):]
        position = 0
    else:
        position = match.end(1)

print(len(content))
