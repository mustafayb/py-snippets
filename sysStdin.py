#!/usr/bin/python3

import sys

if sys.stdin.isatty(): # the isatty method checks if input is from a terminal
    print('Interactively reading data')
    print('Press ^D (ctrl-d) to end input')
data = sys.stdin.readlines() # list of lines of text
data.reverse() # reverse the order of the lines
for line in data:
    print(line, end='')

answer = input('Type your answer: ')
