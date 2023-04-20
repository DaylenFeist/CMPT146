"""Zebrah and ocelot"""
"""
x = int(input())

animals = []
for asd in range(x):
    animals.append(input())
count = 0
while 'O' in animals:
    for i, val in enumerate(animals):
        if val == 'O':
            for index in range(0,i+1):
                if animals[index] == "Z":
                    animals[index] = "O"
            animals[i] = "Z"
            count+=1
            break
print(count)"""

"""
x = int(input())

animals = []
for asd in range(x):
    animals.append(input())

animals.reverse()
value = 1
total = 0
for animal in animals:
    if animal == "O":
        total += value
    value *= 2
print(total)
"""

sets = int(input())


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

for set in range(sets):
    stuff = input().split()
    current_num = stuff[1]
    happy = False


    if not is_prime(int(current_num)):
        current_num = '1'
    while int(current_num) != 1:

        total = 0
        for letter in current_num:
            #print(letter)
            total += int(letter)**2

        if int(stuff[1]) == total or total == 4:
            happy = False
            #print(f'{stuff[1]}unhappy :(')
            break

        if total == 1:
            happy = True
            #print(f'{stuff[1]}Happy :)')
            break
        current_num = str(total)
    #print(stuff[1])
    word = "NO"
    if happy:
        word = "YES"
    print(f"{stuff[0]} {stuff[1]} {word}")