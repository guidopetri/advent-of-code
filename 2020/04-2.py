#! /usr/bin/env python3

import re


def field_valid(field, value):
    if field == 'byr':
        return len(value) == 4 and 1920 <= int(value) and int(value) <= 2002
    if field == 'iyr':
        return len(value) == 4 and 2010 <= int(value) and int(value) <= 2020
    if field == 'eyr':
        return len(value) == 4 and 2020 <= int(value) and int(value) <= 2030
    if field == 'hgt':
        unit = value[-2:]
        value = int(value[:-2])
        if unit == 'cm':
            return 150 <= value and value <= 193
        elif unit == 'in':
            return 59 <= value and value <= 76
    if field == 'hcl':
        return re.match(r'\#[0-9a-f]{6}', value)
    if field == 'ecl':
        return value in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
    if field == 'pid':
        return len(value) == 9
    if field == 'cid':
        return True


with open('04-input.txt', 'r') as f:
    data = f.read().split('\n\n')

fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

valid_passports = 0

for passport in data:
    passport = passport.split()
    passport = {x.split(':')[0]: x.split(':')[1]
                for x in passport}

    if (all([field in passport
             for field in fields])
        and all([field_valid(field, value)
                 for field, value in passport.items()])):
        valid_passports += 1

print(valid_passports)
