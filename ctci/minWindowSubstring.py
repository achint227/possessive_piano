from collections import Counter, defaultdict, deque


def minWindow(s: str, t: str) -> str:
    if len(t) > len(s):
        return ""
    if len(t) == len(s):
        return s if Counter(s) == Counter(t) else ""
    frequencies = defaultdict(int)

    for c in t:
        frequencies[c] += 1

    minlen = float("inf")

    l = -1
    next_match = deque()
    minl, minr = None, None
    for r in range(len(s)):

        if s[r] in frequencies:
            if l == -1:
                l = r
            else:
                next_match.append(r)
            frequencies[s[r]] -= 1
        if all([x < 1 for x in frequencies.values()]):
            currLen = r - l + 1
            if currLen <= minlen:
                minlen = currLen
                minl = l
                minr = r
            if next_match:
                newl = next_match.popleft()
                while next_match and l < newl:
                    if s[l] in frequencies:
                        frequencies[s[l]] += 1
                    l += 1

    return "" if minlen == float("inf") else s[minl : minr + 1]


def main():
    s = "bdab"
    t = "ab"
    result = minWindow(s, t)
    print(result)


if __name__ == "__main__":
    main()
