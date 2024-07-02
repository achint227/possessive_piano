from typing import List


def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2
        print(l, r, mid)
        if nums[mid] == target:
            return mid
        if nums[mid] > target and nums[l] > target:
            l = mid - 1
        else:
            r = mid + 1
    return -1


def main():
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    result = search(nums, target)
    print(f"Index of target: {result}")


if __name__ == "__main__":
    main()
