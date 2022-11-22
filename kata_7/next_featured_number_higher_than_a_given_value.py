"""
Make a function that receives a value, val and outputs the smallest higher number than the given value,
and this number belong to a set of positive integers that have the following properties:

--> their digits occur only once
--> they are odd
--> they are multiple of three
"""


def next_numb(val):
    i = val + 1
    while i <= 9999999999:
        if i % 3 == 0 and i % 2 and len(str(i)) == len(set(str(i))):
            return i
        i += 1
    return 'There is no possible number that fulfills those requirements'
