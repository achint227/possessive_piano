from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

    while top <= bottom:
        mid = (top + bottom) // 2

        if matrix[mid][0] > target:
            bot = mid - 1
        elif matrix[mid][-1] < target:
            top = mid + 1
        else:
            break
     
    mid = (top + bottom) // 2
    while left <= right:
        middle = (left + right) // 2

        if matrix[mid][middle] > target:
            right = middle - 1
        elif matrix[mid][middle] < target:
            left = middle + 1
        else:
            return True
    return False


def main():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3

    result = searchMatrix(matrix, target)
    print(result)

if __name__ == "__main__":
    main()
