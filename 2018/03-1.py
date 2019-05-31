#! /usr/bin/env python

import pandas as pd
import re


def insert_id_into_fabric(instruction, fabric):
    topmost = instruction['top_distance']
    leftmost = instruction['left_distance']
    for ttb_inch in range(topmost, topmost + instruction['height']):
        for ltr_inch in range(leftmost, leftmost + instruction['width']):
            fabric[ttb_inch][ltr_inch] += 1
    return


with open('03-input.txt', 'r') as f:
    content = f.read().split('\n')

# #123 @ 3,2: 5x4
# id @ left,top: width x height

instructions = []
columns = ['id', 'left_distance', 'top_distance', 'width', 'height']
for line in content:
    numbers = []
    for x in re.findall(r'\d+', line):
        numbers.append(int(x))
    instructions.append(numbers)


df = pd.DataFrame(instructions, columns=columns)
# print(df.shape)

fabric = [[0 for y in range(1000)] for x in range(1000)]

df.apply(lambda row: insert_id_into_fabric(row, fabric), axis=1)

fabric_df = pd.DataFrame(fabric)

print(fabric_df.apply(lambda column: sum(column > 1), axis=0).sum())
