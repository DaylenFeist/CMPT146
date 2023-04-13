

"""
A = 0
B = 0
line = input()
line = [line[i:i+2] for i in range(0, len(line), 2)]

for value in line:
    if value[0] == 'A':
        A += int(value[1])
    else:
        B += int(value[1])

    if A > 10 and A > B+1:
        print("A")
        break
    if B > 10 and B > A + 1:
        print("B")
        break
"""
"""
the_input = input()
the_input = the_input.split()

length = int(the_input[0])
code = the_input[1]
guess = the_input[2]

r = 0
q = 0

for x in range(length):
    if code[x] == guess[x]:
        r +=1
for letter in guess:
    if code.count(letter) > 0 and letter in code:
        q += 1
        code = code.replace(letter, '', 1)
print(f"{r} {q-r}")

"""
"""
x = "."
N = int(input())
words = []
if N>= 0 and N <= 50:
    for i in range(0, N):
        words.append(input())
    for data in words:

        letter_s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'x', 'y', 'z']

        for j in [*data]:
            if j.lower() in letter_s:
                letter_s.remove(str(j.lower()))

        if len(letter_s) > 0:
            print("missing ", end="")
            for i in letter_s:
                print(f"{i}",end="")
            print('')
        else:
            print('panagram')"""

