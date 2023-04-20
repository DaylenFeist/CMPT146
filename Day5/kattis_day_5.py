"""Q4
"""
"""
adventures = int(input())

for x in range(adventures):
    money = 0
    incest = 0
    gems = 0

    adventure = input()
    success = "YES"
    for letter in adventure:
        if letter == '$':
            money += 1
        elif letter == '|':
            incest += 1
        elif letter == '*':
            gems += 1
        elif letter == 't':
            incest -= 1
        elif letter == 'j':
            gems -= 1
        elif letter == 'b':
            money -= 1

        if money == -1 or gems == -1 or incest == -1:
            success = "NO"
    if money != 0 or gems != 0 or incest != 0:
        success = "NO"
    print(success)"""


"""
Q3
""""""
import math
paths = int(input())

for asdasdasd in range(paths):
    x = 0
    y = 0
    angle = 90 * math.pi / 180
    instructions = int(input())
    for asd in range(instructions):
        directions = input()
        directions = directions.split()
        direction = (float(directions[0]) * math.pi / 180)
        angle += direction
        distance = float(directions[1])
        x += math.cos(angle) * distance
        y += math.sin(angle) * distance
    print(f"{x} {y}")"""

"""
Q2
"""

#   Grandpa's checkers:
"""
n = int(input(""))
grid = []
for i in range(n):
    grid.append([])
    line = input("")
    for x in line:
        grid[i].append(x)


valid = 1

for i in range(n):
    blackCount = 0
    whiteCount = 0
    for j in range(n):
        # this one checks columns
        if grid[i][j] == "B":
            blackCount += 1
        elif grid[i][j] == "W":
            whiteCount += 1
    if blackCount != whiteCount:
        valid = 0

for j in range(n):
    blackCount = 0
    whiteCount = 0
    # this checks rows
    for i in range(n):
        if grid[i][j] == "B":
            blackCount += 1
        elif grid[i][j] == "W":
            whiteCount += 1
    if blackCount != whiteCount:
        valid = 0


# check for consecutive squares:
for i in range(n):
    count = 0
    for j in range(n-1):
        if grid[i][j] == grid[i][j+1]:
           count += 1
           if count >= 3:
               valid = 0
    if count < 3 and grid[i][j] != grid[i][j+1]:
            count = 0


for j in range(n):
    count = 0
    for i in range(n-1):
        if grid[i][j] == grid[i+1][j]:
           count += 1
           if count >= 3:
               valid = 0
    if count < 3 and grid[i][j] != grid[i+1][j]:
            count = 0


print(valid)
"""


n = int(input(""))
grid = []
valid = 1

for i in range(n):
    grid.append([])
    line = input("")
    for x in line:
        grid[i].append(x)


for i in range(n):
    blackCount = 0
    whiteCount = 0
    for j in range(n):
        # this one checks columns
        if grid[i][j] == "B":
            blackCount += 1
        elif grid[i][j] == "W":
            whiteCount += 1
    if blackCount != whiteCount:
        valid = 0

for j in range(n):
    blackCount = 0
    whiteCount = 0
    # this checks rows
    for i in range(n):
        if grid[i][j] == "B":
            blackCount += 1
        elif grid[i][j] == "W":
            whiteCount += 1
    if blackCount != whiteCount:
        valid = 0

for i in range(n):
    count = 0
    for j in range(n-1):
        if grid[i][j] == grid[i][j+1]:
           count += 1
        if count >= 2:
            valid = 0
        if grid[i][j] != grid[i][j + 1]:
            count = 0
        #print(count)


for j in range(n):
    count = 0
    for i in range(n-1):
        if grid[i][j] == grid[i+1][j]:
           count += 1
        if count >= 2:
            valid = 0
        if grid[i][j] != grid[i + 1][j]:
            count = 0
        #print(count)

print(valid)