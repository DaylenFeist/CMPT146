"""pokechart

letta = input()

numstring = input()
n=3
word = ''
numstring = [int(numstring[i:i+n]) for i in range(0, len(numstring), n)]
for index in numstring:
    index -= 1
    word += letta[index]
print(word)"""

"""das guten"""

"""lights = input()

lights = lights.split()
light1 = int(lights[0])
light2 = int(lights[1])
time = int(lights[2])

for second in range(1, time + 1):
    if second % light1 == 0 and second % light2 == 0:

        print("yes")
        exit()
print('no')"""

"""
stuff = input()

stuff = stuff.split()
total_parts = int(stuff[0])
days = int(stuff[1])

unique_parts = []
for day in range(days):
    part = input()
    if part not in unique_parts:
        unique_parts.append(part)
    if len(unique_parts) >= total_parts:
        print(day + 1)
        exit()
print("paradox avoided")
"""


days = int(input())
junk = input().split()
junk = [ int(x) for x in junk ]

thang = set(junk)
print(junk.index(min(thang)))