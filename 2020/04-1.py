#! /usr/bin/env python3

with open('04-input.txt', 'r') as f:
    data = f.read().split('\n\n')

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid_passports = 0

for passport in data:
    passport = passport.split()
    passport = {x.split(':')[0]: x.split(':')[1]
                for x in passport}

    if all([field in passport for field in fields]):
        valid_passports += 1

print(valid_passports)
