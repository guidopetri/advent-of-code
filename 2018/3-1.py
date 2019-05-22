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
			fabric[tpb_inch][ltr_inch] += 1
	return


df = pd.DataFrame([[int(x) for x in re.findall(r'\d+',line)] for line in content],columns=['id','left_dist','top_dist','width','height'])
#print(df.shape)

fabric = [[0 for y in range(1000)] for x in range(1000)]

df.apply(lambda row:insert_id_into_fabric(row,fabric),axis=1)

fabric_df = pd.DataFrame(fabric)

print(fabric_df.apply(lambda column:sum(column > 1),axis=0).sum())
