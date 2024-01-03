import os


def check_validity(filepath):
    with open(filepath, "r") as f:
        s = f.read()
    stack = []
    if not s:
        return False
    for c in s:
        if c == "{":
            stack.append("*")
        elif c == "}":
            stack.pop()
    return len(stack) == 0


