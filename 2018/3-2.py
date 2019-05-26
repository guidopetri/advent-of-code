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


def check_overlaps(fabric, overlapping_ids):
    for ttb_inch in range(len(fabric)):
        for ltr_inch in range(len(fabric[ttb_inch])):
            if len(fabric[ttb_inch][ltr_inch]) > 1:
                overlapping_ids.update(fabric[ttb_inch][ltr_inch])
    return


with open('3-input.txt', 'r') as f:
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

fabric = [[[] for y in range(1000)] for x in range(1000)]

overlapping_ids = set()

df.apply(lambda row: insert_id_into_fabric(row, fabric), axis=1)
check_overlaps(fabric, overlapping_ids)

# fabric_df = pd.DataFrame(fabric)

print(df[~df['id'].isin(list(overlapping_ids))])
