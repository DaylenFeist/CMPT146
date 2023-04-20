guests = int(input())

guest_list = input()
guest_list = guest_list.split()
guest_list = [ int(x) for x in guest_list ]
awkwardness = guests

for guest_ind in range(guests):
    nextg = guest_ind + 1
    rest = guest_list[nextg:]
    if rest.count(guest_list[guest_ind]) > 0:
        distance = rest.index(guest_list[guest_ind], nextg) - guest_ind + 1
        if distance < awkwardness:
            awkwardness = distance
print(awkwardness)



# School Spirit


"""studentNum = int(input(""))
scores = []
for i in range(studentNum):
    scores.append(input(""))

def calculate_score(scores):
    initialScore = 0
    for i, val in enumerate(scores):
        initialScore += (float(val) * ((4/5)**i))
    initialScore *= (1/5)
    return(initialScore)

print(calculate_score(scores))

sum = 0
count = 0
#print(scores)
for i in range(len(scores)):
    x = scores[0:i] + scores[i+1:]
    sum += calculate_score(x)
    count += 1

print (sum/len(scores))"""

"""
room = input()
room = room.split()

partitions = [0]
partitions_input = input().split()
for x in range(int(room[1])):
    partitions.append(int(partitions_input[x]))
partitions.append(int(room[0]))


unique_val = []
for part in range(len(partitions)):
    for partition2 in partitions[part+1:]:
        distance = (partition2 - partitions[part])
        if distance not in unique_val:
            unique_val.append(distance)

unique_val.sort()
for val in unique_val:
    print(val, end=" ")
"""