def kEmptySlots(bulbs, k):

    bulb_set = set()
    res = 0

    def allEmpty(left, right):
        for i in range(left + 1, right):
            if i in bulb_set:
                return False
            return True

    for bulb in bulbs:
        bulb_set.add(bulb)

        if bulb - k - 1 in bulb_set and allEmpty(bulb - k - 1, bulb):
            res += 1
        if bulb + k + 1 in bulb_set and allEmpty(bulb, bulb + k + 1):
            res += 1

    return res if res else -1


if __name__ == "__main__":
    bulbs = [1, 3, 2]
    k = 1
    result = kEmptySlots(bulbs, k)
    print(f"Number of empty slots: {result}")
