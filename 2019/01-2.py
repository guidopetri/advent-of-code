#! /usr/bin/env python3


def get_fuel(x):
    return (int(x) // 3) - 2


with open('01-input.txt', 'r') as f:
    modules = f.readlines()

fuel_req = 0

# sample input
# modules = ['12', '14', '1969', '100756']

for module in modules:
    fuel = get_fuel(module)
    new_fuel = fuel
    while new_fuel > 0:
        new_fuel = max(get_fuel(new_fuel), 0)
        fuel += new_fuel
    fuel_req += fuel

print(fuel_req)
