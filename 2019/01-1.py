#! /usr/bin/env python3

with open('01-input.txt', 'r') as f:
    modules = f.readlines()

fuel_req = 0

# sample input
# modules = ['12', '14', '1969', '100756']

for module in modules:
    fuel_req += (int(module) // 3) - 2

print(fuel_req)
