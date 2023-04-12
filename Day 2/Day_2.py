"""
Day 2 of CMPT146
"""


# Mistakes we have possibly made in relation to references.
def Ex_1():
    x = [1, 2, 3]
    y = x
    y.append(4)
    print(x)
    # The list of X is also changed to be the same as y.
def Ex_2():
    x = [[1, 2], [3, 4]]
    copy = []
    for val in x:
        copy.append(val)
        copy[0][0] = 42
    print(x)
    # The value of x[0][0] is also changed to 42

"""
Why is this??
                REFERENCES!!!!
Variables have 3 aspects.
    Name
    Value
    Address
    
Frame Diagrams
    Code
    x = 3
    y = 4
    Simplified frame representation
    x | 0x10397e78b
    y | 0x10397e84b
    Frame Diagram
    x | ------> 3
    y | ------> 4

The reason that these things seem to be weird is that

int, string, bool etc are immutable,
but lists are kind of like this

    Frame Diagram
    list | -------> [[----> value1] [------> value2]]
so inside, the list points to a box
and that box points to each value of that list, which we can edit

### more frame diagrams saved as photos

ULTIMATE RULES!!!

1) Literals and expressions create **NEW OBJECTS** 
    expression is like (x + 1)
    Literal is just a value, 3, True
2) Only method calls on mutable objects can change existing object
    METHODS CHANGE 
3) Only assignment statements can change a reference
    ONLY = MOVES ARROW
"""
def Ex_3():

    x = [1, 2, 3]
    y = x
    y.append('four')
    # refer to drawing for beautiful output!

"""
Functions are similar
    def func
actually defines an object named "func", which points to the directions inside
when it is called, it goes inside, and it creates a kinda inner table (diagram)

"""
def Ex_4():
    def tagteam(m):
        m = 'Mothra'

    m = "Godzilla"
    tagteam(m)
    print(m)
    #frame diagram as shown in Ex_4


"""
x = [[1,2], [3,4]]
x | > [ -->[-> 1, -> 2], -->[-> 3, -> 4]]
copy | [ same inner lists :)]
changes the 1 which copy points to, but x also points to that 1, so then it is changed for both. yippie!!!
"""