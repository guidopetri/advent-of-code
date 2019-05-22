#! /usr/bin/env python

import os
import numpy as np
import pandas as pd
import re

pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

#read input
with open('5-input.txt','r') as f:
	content = f.read()

re_string = re.compile(r'(\w)(\1)',flags=re.IGNORECASE)
position=0

while re_string.search(content,position) != None:
	match = re_string.search(content,position)
	if match.group(1) != match.group(2):
		content = content[:match.start(1)]+content[match.end(2):]
		position = 0
	else:
		position = match.end(1)

print(len(content))
