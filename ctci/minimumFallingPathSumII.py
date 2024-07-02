from typing import List


def minFallingPathSum(matrix: List[List[int]]) -> int:
    NROWS = len(matrix)
    NCOLS = len(matrix[0])
    dp = {}

    def helper(row, col):
        if row >= NROWS:
            return 0
        if col < 0 or col >= NCOLS:
            return float("inf")
        if (row, col) in dp:
            return dp[(row, col)]

        dp[(row, col)] = matrix[row][col] + min(
            [helper(row + 1, new_col) for new_col in range(NCOLS) if new_col != col]
        )
        return dp[(row, col)]

    return min([helper(0, col) for col in range(NCOLS)])


def main():
    # Example usage
    matrix = [[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
    result = minFallingPathSum(matrix)
    print("Minimum falling path sum:", result)

if __name__ == "__main__":
    main()


