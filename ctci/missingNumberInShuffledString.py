'''
Given a string 's' consisting of digits containing numbers from 1 to 'n', find the missing number from the string 
n < 100
'''
from random import shuffle

def find_missing(s, n):

    expected_sum = (n * (n + 1)) // 2
    res = 0
    seen = set()

    def dfs(i=0, curr_sum=0, count=0):
        nonlocal expected_sum, res

        if i == len(s):
            if count == n - 1:
                res = expected_sum - curr_sum
                return True

        num = int(s[i: i + 2])
        one_digit = two_digit = False
        if num <= n and num not in seen:
            seen.add(num)
            two_digit = dfs(i + 2, curr_sum + num, count + 1)
            seen.remove(num)

        num = int(s[i])
        seen.add(num)
        one_digit = dfs(i + 1, curr_sum + num, count + 1)
        seen.remove(num)

        return one_digit or two_digit

    dfs()

    return res

nums = [str(x) for x in range(1, 16) if x != 15]


shuffle(nums)
print("".join(nums))
print(find_missing("".join(nums), 99))



        




