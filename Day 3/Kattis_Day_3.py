"""
Question 2
"""
"""
userstuff = input()
mode = userstuff[0]
data = userstuff[2:]

if mode == 'E':
    count = 1
    new_word = ''
    previous_letter = data[0]
    for letter in data[1:]:
        if letter == previous_letter:
            count += 1
        else:
            if count > 0:
                new_word += previous_letter
                new_word += str(count)
                count = 1
        previous_letter = letter
    new_word += previous_letter
    new_word += str(count)
    print(new_word)


if mode == 'D':
    data = [data[i:i + 2] for i in range(0, len(data), 2)]
    new_word = ''
    for letter_num in data:
        for x in range(int(letter_num[1])):
            new_word += letter_num[0]
    print(new_word)
"""

"""
Kattis Q3
"""


stuff = []
knights = 0
for x in range(5):
    stuff.append(input())
knight_pos = []
for row in range(5):
    for col in range(5):
        if stuff[row][col] == 'k':
            knights += 1
            knight_pos.append(row+1+col+1)
even = 0
odd = 0
for knight in knight_pos:
    if knight % 2 == 0:
        even += 1
    else:
        odd += 1

if (even +1 == odd or even -1 == odd or even == 0 or odd == 0) and knights == 9:
    print("valid")
else:
    print('invalid')


"""
stuff = []
for x in range(5):
    stuff.append(input())
def try_spot(x,y,stuff):
    try:
        #print(f"{x},{y}")
        if y < 0 or x < 0:
            return ''
        if stuff[y][x] == 'k':
            #print(stuff)
            return 'invalid'
        return ''
    except:
        return ''

collision = ''
knight = 0
for row in range(5):
    for col in range(5):
        if stuff[row][col] == 'k':
            knight += 1
            #check all valid spots
            collision += try_spot(col-1, row-2, stuff)
            collision += try_spot(col + 1, row - 2, stuff)
            collision += try_spot(col - 2, row - 1, stuff)
            collision += try_spot(col + 2, row - 1, stuff)
            collision +=try_spot(col - 2, row + 1, stuff)
            collision +=try_spot(col - 2, row - 1, stuff)
            collision +=try_spot(col - 1, row + 2, stuff)
            collision +=try_spot(col + 1, row + 2, stuff)
if len(collision) != 0 or knight != 9:
    print("invalid")
else:
    print('valid')

"""