"""
Chapter 15: Nodes

A node is a datatype that stores two things,

    1) Any Data Value
    2) A refrence to another Node or None

Why?
    Building block for data squences,
    think list



Single node is not useful
    Chained together they are
    anode = node (1 , None )
    bnode = node (2 , anode )

"""

import node as N
code = N.node(3, N.node(0, N.node(6)))

anode = code.get_next()
bnode = N.node(1, anode)
code.set_next(bnode)

print(code.get_data())
print(code.get_next().get_data())