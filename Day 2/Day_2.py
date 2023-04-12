"""
Day 2 of CMPT146
"""


# Mistakes we have possibly made in relation to references.

x = [1, 2, 3]
y = x
y.append(4)
print(x)
# The list of X is also changed to be the same as y.

