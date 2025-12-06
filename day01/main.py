import os
import math

dir_path = os.path.abspath(__file__)
dir_path = os.path.dirname(dir_path)

file_path = dir_path + '/test.txt'

START_POSITION = 50
DIAL_SIZE = 100

# --- Part One ---
password = 0

with open(file_path, 'r', encoding='utf-8') as file:
    dial = START_POSITION
    
    for line in file:
        direction = line[0]
        click = int(line[1:])

        if click == 0: continue
        
        old_dial = dial

        if direction == 'R':
            dial += click 
        else: 
            dial -= click

        dial = dial % DIAL_SIZE
        if dial == 0:
            password += 1

    print(f"Answer Part One : {password}")

# --- Part Two ---
password = 0

with open(file_path, 'r', encoding='utf-8') as file:
    dial = START_POSITION
    
    for line in file:
        direction = line[0]
        click = int(line[1:])

        if click == 0: continue
        
        old_dial = dial

        if direction == 'R':
            dial += click
            hits = (dial // DIAL_SIZE) - (old_dial // DIAL_SIZE)
        else: 
            dial -= click
            hits = ((old_dial - 1) // DIAL_SIZE) - ((dial - 1) // DIAL_SIZE)    

        password += hits

    print(f"Answer Part Two : {password}")
