from typing import List


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        print(l, r, mid)
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        elif nums[mid] >= nums[l]:
            l = mid
        else:
            r = mid - 1


def main():
    nums = [11,13,15,17]
    result = findMin(nums)
    print("Minimum element:", result)


if __name__ == "__main__":
    main()
