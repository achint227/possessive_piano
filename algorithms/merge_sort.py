def mergeback(arr, left_start, right_start, right_end):
    helper = [0] * (right_end - left_start + 1)
    left_index = left_start
    right_index = right_start
    for i in range(len(helper)):
        if (
            right_index > right_end
            or left_index < right_start
            and arr[left_index] <= arr[right_index]
        ):
            helper[i] = arr[left_index]
            left_index += 1
        else:
            helper[i] = arr[right_index]
            right_index += 1
    return helper


def copyback(arr, helper, offset):
    for i in range(len(helper)):
        arr[i + offset] = helper[i]


def merge_sort_helper(arr, l, r):
    if l == r:
        return
    mid = (l + r) // 2
    merge_sort_helper(arr, l, mid)
    merge_sort_helper(arr, mid + 1, r)
    helper = mergeback(arr, l, mid + 1, r)
    copyback(arr, helper, l)


def merge_sort(arr):
    merge_sort_helper(arr, 0, len(arr) - 1)




def main():
    arr = [5, 2, 9, 1, 7, 3]
    print("Original array:", arr)
    merge_sort(arr)
    print("Sorted array:", arr)


if __name__ == "__main__":
    main()
