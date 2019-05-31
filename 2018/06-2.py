#! /usr/bin/env python

import pandas as pd


pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

# read input
with open('06-input.txt', 'r') as f:
    content = f.read().split('\n')

content_tuples = []

for line in content:
    content_tuples.append(tuple(line.split(', ')))

content_tuples = [(int(x), int(y)) for x, y in content_tuples]

# 400x400 should be enough for our purposes

df = pd.DataFrame([[[] for x in range(400)] for y in range(400)])

for y in range(400):
    for x in range(400):
        distances = [(abs(tup[0] - x)
                      + abs(tup[1] - y)
                      ) for tup in content_tuples]
        summed_distance = sum(distances)
        df.iat[x, y] = True if summed_distance < 10000 else False

counts = []

for series in df.columns:
    counts.append(df[series].value_counts())

new_df = pd.DataFrame(pd.concat(counts, axis=0))

new_df.reset_index(drop=False, inplace=True)
new_df.columns = ['index', 'counts']

totals = new_df.groupby('index').agg({'counts': 'sum'})
totals.sort_values(by='counts', ascending=False, inplace=True)

print(totals)
