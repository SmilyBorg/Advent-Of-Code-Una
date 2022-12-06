#!/usr/bin/env python3

def read_line(fname):
    for line in open(fname):
        yield (line.split())
 
 
def read_elves(fname):
    elf = 0
    elves = [[]]       
    for value in (read_line(fname)):
        if len(value) == 0 :
            # Move to the next elf
            elf = elf + 1
            elves.append([])
        else:
            #collect each elf
            elves[elf].append(value[0])
    return (elves)

def totals(fname):
    totals=[]
    for (elf, bag) in enumerate(read_elves(fname)):
        #print(elf, " ", len(bag))
        total=0
        for calories in bag:
            total=int(total)+int(calories)
        totals.append(total)
    return totals

def max_calories(fname):
    max=0
    for x in totals(fname):
        if x > max:
            max = x
    return max

print(max_calories('input'))

 
        
    
