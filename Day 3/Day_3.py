"""
Day 3 of CMPT146
"""

"""
Chapter 4: Design Goals

Correctness:
    -The program does what it is supposed to do
    -The program does not do what it is not supposed to do

Efficiency: 
    -It is better to minimize resource usage
        For us, this would be primarily time, and memory.
        
Robustness:
    -What to do when things go wrong???? Invalid inputs, etc Sqrt(-1) whaaaaaaa
        Dont crash please :)
        maybe inform user to try again
        
Adaptability:
    - Problem Changes???
        How easy is it to change it up a bit

Reusability:
    Can you easily use the same piece of code in another project 
        If yes, the code is likely better

Two categories
    Quantitative
        Correctness, Efficiency
    Qualitative
        Robustness, Adaptability, Reusability
"""
#Command line parameters
def cmd_line():
    import sys

    n = int(sys.argv[1])

    print(n)
#you can run this from the command line
cmd_line()

"""
CHAPTER 6

kinda documenting

Purpose: what the function does. simple concise...

Pre-Condition: what you are passing in. types, what they should be...

Post-Conditions: does it print anything, console input, or modify any of its parameters 

Return: what it returns, types...

"""

"""
Chapter 7

Software errors != software faults



"""