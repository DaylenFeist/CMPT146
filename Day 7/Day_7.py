"""
Chapter 18: The Four Abstractions


#1
Time
    not runtime, measure time in terms of computational steps.


#2
something


#3
Categories
    number of computational steps is hard notice the difference
        3N + 10
        3 N + 20
    cant measure that distance, so instead we place it in a category
        3N + 10 = O(N)
        3N^2 + 10 = O(N^2)
    are in different categories

    one of a bunch of categories

    O(1) < O(log2N) < O(N) < O(Nlog2N) < O(N^2)... O(2^N)... O(N^N)

#4
Worst-Case Behavior

    Always follow the if statement that takes you down the longest path
"""