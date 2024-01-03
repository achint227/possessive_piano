"""
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""


def is_unique(s: str) -> bool:
    charSet = set()

    for char in s:
        if char in charSet:
            return False
        charSet.add(char)
    return True


def is_unique_no_additional_space(s: str) -> bool:
    s = list(s).sort()

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True


