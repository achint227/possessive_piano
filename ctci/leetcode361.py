"""
    enemyCountGrid = [[0] * COLS] * ROWS

    def increaseCounts(r, c):
        


    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "E":
                increaseCounts(r, c)
    return max(max(enemyCountGrid))


"""


def bombEnemy(grid):

    ROWS = len(grid)
    COLS = len(grid[0])
    maxKilled = 0

    def getEnemies(r, c):
        res = 0
        for row in range(r, -1, -1):
            if grid[row][c] == "W":
                break
            if grid[row][c] == "E":
                res += 1
        for row in range(r, ROWS):
            if grid[row][c] == "W":
                break
            if grid[row][c] == "E":
                res += 1
        for col in range(c, -1, -1):
            if grid[r][col] == "W":
                break
            if grid[r][col] == "E":
                res += 1
        for col in range(c, COLS):
            if grid[r][col] == "W":
                break
            if grid[r][col] == "E":
                res += 1
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == "0":
                killed = getEnemies(r, c)
                maxKilled = max(maxKilled, killed)
    return maxKilled


def main():
    # Define the grid
    grid = [["0"] + ["E"] * 10 + ["W"]]

    # Call the bombEnemy function
    result = bombEnemy(grid)

    # Print the result
    print("Maximum number of enemies killed:", result)


# Call the main function
if __name__ == "__main__":
    main()
