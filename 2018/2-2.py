#! /usr/bin/env python

# open our file
with open('2-input.txt', 'r') as f:
    # read the content of the input file and split it into a list
    # each element is one line
    content = f.read().split('\n')

# initialize a "counts" dictionary
counts = {}

# for each character in the length of the strings
for char in range(len(content[0])):
    # create a trimmed version of each one of the strings
    # this is done by slicing up until the character index in question, then
    # adding the rest of the string, skipping the character index in question
    content_trimmed = [box[:char] + box[char + 1:] for box in content]
    # print the trimmed version of the first string in the list
    print(content_trimmed[0])

    # print the list that has all the strings if the count of the string > 1
    # .count() gives us the count of each element in the list. if there is a
    # duplicate, count() will show us a number greater than 1
    print([box for box in content_trimmed if content_trimmed.count(box) > 1])
