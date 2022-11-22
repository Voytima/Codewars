"""
Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.
"""


def is_anagram(test, original):
    if len(test) != len(original):
        return False
    return sorted(test.lower()) == sorted(original.lower())
