#! /usr/bin/env python

import os
import numpy as np
import pandas as pd
import re

with open('3-input.txt','r') as f:
	content = f.read().split('\n')

##123 @ 3,2: 5x4
#id @ left,top: width x height

def insert_id_into_fabric(df_row,fabric):
	for tpb_inch in range(df_row['top_dist'],df_row['top_dist']+df_row['height']):
		for ltr_inch in range(df_row['left_dist'],df_row['left_dist']+df_row['width']):
			fabric[tpb_inch][ltr_inch].append(df_row['id'])
	return

def check_overlaps(fabric,overlapping_ids):
	for tpb_inch in range(len(fabric)):
		for ltr_inch in range(len(fabric[tpb_inch])):
			if len(fabric[tpb_inch][ltr_inch]) > 1:
				overlapping_ids.update(fabric[tpb_inch][ltr_inch])
	return

df = pd.DataFrame([[int(x) for x in re.findall(r'\d+',line)] for line in content],columns=['id','left_dist','top_dist','width','height'])
#print(df.shape)

fabric = [[[] for y in range(1000)] for x in range(1000)]

overlapping_ids = set()

df.apply(lambda row:insert_id_into_fabric(row,fabric),axis=1)
check_overlaps(fabric,overlapping_ids)

#fabric_df = pd.DataFrame(fabric)

print(df[~df['id'].isin(list(overlapping_ids))])
