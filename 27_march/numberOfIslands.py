def numIslands(grid) -> int:
    m, n = len(grid), len(grid[0])
    def dfs(i, j):
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0:
            return
        grid[i][j] = 0
        dfs(i + 1, j)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i, j - 1)
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                dfs(i, j)
                res += 1
    return res

def main():
    n, m = int(input()), int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    print(numIslands(grid))


if __name__ == "__main__":
    main()