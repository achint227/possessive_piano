from collections import defaultdict


def checkInclusion(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False
    d = defaultdict(int)

    for c in s1:
        d[c] += 1
    for i in range(len(s1)):
        d[s2[i]] -= 1

    print(len(s2)-len(s1))
    for i in range(0, len(s2) - len(s1)):
        print(s2[i], s2[i + len(s1)])
        d[s2[i]] += 1
        d[s2[i + len(s1)]] -= 1
        if all([x == 0 for x in d.values()]):
            return True

    return False


def main():
    s1 = "adc"
    s2 = "dcda"
    result = checkInclusion(s1, s2)
    print(result)


if __name__ == "__main__":
    main()
