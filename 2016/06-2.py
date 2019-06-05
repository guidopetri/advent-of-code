#! /usr/bin/env python

import pandas as pd


with open('06-input.txt', 'r') as f:
    data = f.read()

example = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""

df = pd.DataFrame([list(x) for x in data.split('\n')])

solution = []

for col in df:
    solution.append(df[col].value_counts(ascending=True).index[0])

print(''.join(solution))
