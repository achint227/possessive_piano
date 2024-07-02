from typing import List


def partitionLabels(s: str) -> List[int]:
    last_occurence = {}

    for i, c in enumerate(s):
        last_occurence[c] = i

    res = []
    curr = 0
    end = 0
    start = 0
    while curr<len(s) and end < len(s):
        end = max(end,last_occurence[s[curr]])
        if curr == end:

            res.append(end - start + 1)
            start = curr+1

        curr += 1
    return res


if __name__ == "__main__":
    s = "ab"
    result = partitionLabels(s)
    print(result)
