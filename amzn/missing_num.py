"""
Given a string with numbers from 1 to n in some arbitrary order, find the missing number.
n < 100

Example:
Input: "617352"
Output: 4
"""
from random import shuffle, randint

def missing_number(n: int, s: str) -> int:
    
    expected_sum = (n * (n + 1)) // 2

    print(f"Expected sum -> {expected_sum}")

    seen = set()


    def backtrack(i, remaining, remaining_sum):

        print(f"Checking index {i} with {remaining} elements left and remaining sum = {remaining_sum}")

        if i == len(s) and remaining == 1:
            print(f"found answer to be {remaining_sum}")
            return remaining_sum

        move_one = move_two = 0

        if i < len(s):
            take_one = int(s[i])

            if take_one <= n and remaining_sum > take_one and take_one not in seen:
                print(f"checking number {take_one} by considering one digit")
                seen.add(take_one)
                move_one = backtrack(i + 1, remaining - 1, remaining_sum - take_one)
                seen.remove(take_one)
        
        if move_one:
            return move_one
        
        if i + 1 < len(s):
            take_two = int(s[i: i+2])
            if take_two <= n and remaining_sum > take_two and take_two not in seen:
                print(f"checking number {take_two} by considering two digits")

                seen.add(take_two)
                move_two = backtrack(i + 2, remaining - 1, remaining_sum - take_two)
                seen.remove(take_two)
        
        if move_two:
            return move_two
        
        return 0


    return backtrack(0, n, expected_sum)


def test(n):

    r = randint(1,n)

    print(f"random number ->{r}")

    l = list(str(x) for x in range(1,n+1) if x != r)
    shuffle(l)

    s = "".join(l)

    print(f"shuffled string -> {s}")

    res = missing_number(n, s)
    print(res)

    assert res == r


test(99)







        





