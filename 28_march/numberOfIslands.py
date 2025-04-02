from collections import deque

def numDistinctIslands(grid):
    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    distinct_islands = set()

    def dfs(r, c, base_r, base_c):
        stack = [(r, c)]
        shape = []
        while stack:
            x, y = stack.pop()
            if not (0 <= x < n and 0 <= y < m) or visited[x][y] or grid[x][y] == 0:
                continue
            visited[x][y] = True
            shape.append((x - base_r, y - base_c))  
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  
                stack.append((x + dx, y + dy))
        return shape

    def normalize(shape):
        transformations = []
        shape = sorted(shape)  
        for _ in range(4): 
            shape = sorted([(y, -x) for x, y in shape])  
            transformations.append(tuple(shape))  
            reflections = [(x, -y) for x, y in shape], [(-x, y) for x, y in shape]
            for ref in reflections:
                transformations.append(tuple(sorted(ref)))
        return min(transformations)  

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                shape = dfs(i, j, i, j)
                distinct_islands.add(normalize(shape))

    return len(distinct_islands)

n = int(input())
m = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

print(numDistinctIslands(grid))
