#! /usr/bin/env python

import re


def aba(string):
    if re.search(r'(.)((?!\1).)\1', string):
        return True
    return False


with open('07-input.txt', 'r') as f:
    data = f.read()

ssl_count = 0

example1 = 'aba[bab]xyz'
example2 = 'zazbz[bzb]cdb'

for ip in data.split('\n'):
    ssl = False
    hypernet_strings = re.findall(r'(?<=\[)(.+?)(?=\])', ip)
    clean_ip = re.sub(r'\[.+?\]', r'\|', ip)
    supernet_strings = clean_ip.split('|')

    for string in supernet_strings:
        for match in re.finditer(r'(.)(?=(?!\1)(.)\1)', string):
            opposite = match.group(2) + match.group(1) + match.group(2)
            if any(opposite in hypernet for hypernet in hypernet_strings):
                ssl = True

    if ssl:
        ssl_count += 1

print('SSL supporting IPs: {}'.format(ssl_count))
