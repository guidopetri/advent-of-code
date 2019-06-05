#! /usr/bin/env python

with open('09-input.txt', 'r') as f:
    data = f.read()

in_repetition = False

status = 'reading'
rep_chars = []
char_count = []
char_counter = 0
rep_count = []
rep_counter = 0

decompressed = []

for character in data:
    if character == '(' and not in_repetition:
        in_repetition = True
        status = 'charcount'
    elif status == 'charcount':
        if character != 'x':
            char_count.append(character)
        else:
            char_counter = int(''.join(char_count))
            char_count = []
            status = 'times'
    if status == 'times':
        status = 'number'
    elif status == 'number':
        if character != ')':
            rep_count.append(character)
        else:
            rep_counter = int(''.join(rep_count))
            status = 'end'
    if status == 'end' and character == ')':
        status = 'reading'
        continue

    if status == 'reading':
        if char_counter > 0:
            rep_chars.append(character)
            char_counter -= 1
        if char_counter == 0:
            if rep_counter > 0:
                for x in range(rep_counter):
                    decompressed += rep_chars
                rep_counter = 0
                rep_count = []
                rep_chars = []
                in_repetition = False
            else:
                decompressed += character

print(len(decompressed))
