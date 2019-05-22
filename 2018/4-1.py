#! /usr/bin/env python

import os
import numpy as np
import pandas as pd
import re
import datetime

pd.options.display.max_rows = 999
pd.options.display.max_columns = 999

#read input
with open('4-input.txt','r') as f:
	content = f.read().split('\n')

# [1518-09-22 23:50] Guard #2309 begins shift

#create a table
df = pd.DataFrame([[event[1:17],event[19:]] for event in content],columns=['Timestamp of event','Event'])

#sorting by time
df['Timestamp of event'] = df.apply(lambda x:datetime.datetime.strptime(x['Timestamp of event'],'%Y-%m-%d %H:%M')-datetime.timedelta(hours=1),axis=1)
df.sort_values(by='Timestamp of event',ascending=True,inplace=True)

#find the guard ID
df['guard_id'] = df['Event'].str.extract(r'Guard #(\d+)')
#propagate it forward
df['guard_id'].fillna(method='ffill',inplace=True)

#find event booleans
df['fell_asleep'] = df['Event'].str.contains(r'falls asleep')
df['woke_up'] = df['Event'].str.contains(r'wakes up')
df['status'] = df['fell_asleep']*1+df['woke_up']*0

df['Minute of event'] = df.apply(lambda x:datetime.datetime.strftime(x['Timestamp of event'],'%M'),axis=1)
df['Date of event'] = df.apply(lambda x:datetime.datetime.strftime(x['Timestamp of event'],'%Y-%m-%d'),axis=1)

pivoted_df = df.pivot_table(values='status',index=['Date of event','guard_id'],columns=['Minute of event'])
pivoted_df.fillna(method='ffill',axis=1,inplace=True)
pivoted_df.reset_index(drop=False,inplace=True)
pivoted_df['total_asleep_min'] = pivoted_df.sum(axis=1)

grouped_df = pivoted_df.groupby(['guard_id']).agg({'total_asleep_min':'sum'})
grouped_df.sort_values(by='total_asleep_min',ascending=False,inplace=True)

print('\nguard who slept the most:\n')
print(grouped_df.head(1))

sliced_df = pivoted_df[pivoted_df['guard_id'] == grouped_df.iloc[:1,:].index.values[0]].drop(['Date of event','guard_id','total_asleep_min'],axis=1)
print('\nminute during which guard most slept:\n')
print(int(sliced_df.sum().idxmax()))

print('\nsolution: %s' % (int(grouped_df.iloc[:1,:].index.values[0])*int(sliced_df.sum().idxmax())))
