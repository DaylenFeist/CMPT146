
"""
questino 4
"""
"""
stuff = input()
stuff = stuff.split()
max_capacity = int(stuff[0])
stations = int(stuff[1])

train_cap = 0
if stations == 0:
    print('impossible')
    exit()
for x in range(stations):
    data = input()
    data = data.split()
    exit_num = int(data[0])
    enter = int(data[1])
    wait = int(data[2])

    train_cap = train_cap + enter - exit_num
    if (wait != 0 and max_capacity != train_cap) or train_cap < 0 or train_cap > max_capacity:
        print('impossible')
        exit()
if train_cap == 0:

    print('possible')
else:
    print('impossible')"""
#should work but doesnt :(

#if it ends the day at !0
#if it has a negative numberof passengers ever
#if people wait even if there is

#Question 3
"""
dim = input()
dim = dim.split()
x = int(dim[1])
y = int(dim[0])
square = []
for rows in range(y):
    string = input()
    square.append([])
    for col in range(x):
        if string[col] == '#':
            square[rows].append(True)
        else:
            square[rows].append(False)


def search(row, col):
    found_something = False
    count = 0
    for y in range(-1,2):
        for x in range(-1,2):
            try:
                if square[row + y][col + x]:
                    #print(count)
                    count = 1
                    square[row + y][col + x] = False
                    count += search(row + y,col + x)
                    found_something = True
            except:
                pass
count = 0
for row in range(len(square)):
    for col in range(len(square[row])):
        if square[row][col]:
            square[row][col] = False
            #print(search(row, col))
            search(row, col)
            count += 1
print(count)
#doesnt work but not sure why
"""
"""
win = 0
battles = int(input())
for battle in range(battles):
    thang = input()
    previous_letter = ''
    lost = False
    for letter in thang:
        if letter == "D" and previous_letter == "C":
            lost = True
        previous_letter = letter
    if lost != True:
        win += 1
print(win)""" #works!

import math
number = input()
data = number.split()
rounds = int(data[1]) +int(data[2])
serves = int(data[0])
new = rounds/serves

new = math.floor(new)

if new % 2 != 0:
    print("opponent")
else:
    print("paul")
