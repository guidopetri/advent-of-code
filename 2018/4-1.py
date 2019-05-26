#! /usr/bin/env python

import pandas as pd
from datetime import datetime, timedelta


def get_timestamp(x):
    timestamp = datetime.strptime(x['Timestamp of event'], '%Y-%m-%d %H:%M')
    return timestamp - timedelta(hours=1)


def get_minute(x):
    return datetime.strftime(x['Timestamp of event'], '%M')


def get_date(x):
    return datetime.strftime(x['Timestamp of event'], '%Y-%m-%d')


# read input
with open('4-input.txt', 'r') as f:
    content = f.read().split('\n')

# [1518-09-22 23:50] Guard #2309 begins shift

# create a table
df = pd.DataFrame([[event[1:17], event[19:]] for event in content],
                  columns=['Timestamp of event', 'Event'])

# sorting by time
df['Timestamp of event'] = df.apply(get_timestamp, axis=1)
df.sort_values(by='Timestamp of event', ascending=True, inplace=True)

# find the guard ID
df['guard_id'] = df['Event'].str.extract(r'Guard #(\d+)')
# propagate it forward
df['guard_id'].fillna(method='ffill', inplace=True)

# find event booleans
df['fell_asleep'] = df['Event'].str.contains(r'falls asleep')
df['woke_up'] = df['Event'].str.contains(r'wakes up')
df['status'] = df['fell_asleep'] * 1 + df['woke_up'] * 0

df['Minute of event'] = df.apply(get_minute, axis=1)
df['Date of event'] = df.apply(get_date, axis=1)

pivoted_df = df.pivot_table(values='status',
                            index=['Date of event', 'guard_id'],
                            columns=['Minute of event'])

pivoted_df.fillna(method='ffill', axis=1, inplace=True)
pivoted_df.reset_index(drop=False, inplace=True)
pivoted_df['total_asleep_min'] = pivoted_df.sum(axis=1)

grouped_df = pivoted_df.groupby(['guard_id']).agg({'total_asleep_min': 'sum'})
grouped_df.sort_values(by='total_asleep_min', ascending=False, inplace=True)
sleepy_guard = grouped_df.iloc[:1, :].index.values[0]

print('\nguard who slept the most:\n')
print(sleepy_guard)

sliced_df = pivoted_df[pivoted_df['guard_id'] == sleepy_guard]
sliced_df.drop(['Date of event', 'guard_id', 'total_asleep_min'], axis=1)
print('\nminute during which guard most slept:\n')
print(int(sliced_df.sum().idxmax()))

print('\nsolution: %s' % (int(sleepy_guard) * int(sliced_df.sum().idxmax())))
