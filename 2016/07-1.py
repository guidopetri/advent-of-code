#! /usr/bin/env python

import re


def abba(string):
    if re.search(r'(.)((?!\1).)\2\1', string):
        return True
    return False


with open('07-input.txt', 'r') as f:
    data = f.read()

tls_count = 0

example1 = 'cabbage[mnop]qrst'
example2 = 'aaaa[qwer]tyui'

for ip in data.split('\n'):
    abba_hypernet = False
    tls = False
    for match in re.finditer(r'(?<=\[)(.+?)(?=\])', ip):
        if abba(match.group(1)):
            abba_hypernet = True
    if not abba_hypernet:
        clean_ip = re.sub(r'\[.+?\]', r'\|', ip)
        for substring in clean_ip.split('|'):
            if abba(substring):
                tls = True
    if tls:
        tls_count += 1

print('TLS supporting IPs: {}'.format(tls_count))
