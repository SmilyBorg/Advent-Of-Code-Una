#!/usr/bin/env python3

def read_line(fname):
    for line in open(fname):
        yield (line.split())

def rock_paper_scissors(opponent, player):
    if opponent == 'A' and response == 'Y':
        return 8
    elif opponent == 'B' and response == 'Z':
        return 9
    elif opponent == 'C' and response == 'X':
        return 7
    elif opponent == 'A' and response == 'X':
        return 4
    elif opponent == 'B' and response == 'Y':
        return 5
    elif opponent == 'C' and response == 'Z':
        return 6
    elif opponent == 'A' and response == 'Z':
        return 3
    elif opponent == 'B' and response == 'X':
        return 1
    elif opponent == 'C' and response == 'Y':
        return 2

score = 0        
for (opponent, response) in read_line('input'):
    score = score + rock_paper_scissors(opponent, response)

print (score)
