def exist(grid, word: str) -> bool:
    ROWS = len(grid)
    COLS = len(grid[0])

    def dfs(r, c, i, visited):
        if i == len(word):
            return True
        if (
            0 <= r < ROWS
            and 0 <= c < COLS
            and (r, c) not in visited
            and word[i] == grid[r][c]
        ):
            visited.add((r, c))
            neighbors = [[r, c + 1], [r + 1, c], [r - 1, c], [r, c - 1]]
            for r1, c1 in neighbors:
                if dfs(r1, c1, i + 1, visited):
                    return True
        return False

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == word[0]:
                if dfs(r, c, 0, set()):
                    return True
    return False


def main():
    grid = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    word = "ABCEFSADEESE"
    result = exist(grid, word)
    print(result)


if __name__ == "__main__":
    main()
