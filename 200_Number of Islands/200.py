# BFS - Breadth-first Search
# 一直找 找的是对的
from collections import deque
def numIslands(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    islands = 0
    rows, cols = len(grid), len(grid[0])
    q, visit = deque(), set()

    def bfc(r, c):
        q.append((r, c))
        while q:  # while deque is not empty
            row, col = q.popleft()
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, down, up
            for dr, dc in direction:
                r, c = row+dr, col+dc
                if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visit:
                    q.append((r, c))
                    visit.add((r, c))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visit:
                islands += 1
                bfc(r, c)
    return islands

# DFS - Depth-first Search
# 找到不符合条件的值时返回继续找新的
def numIslands2(grid):
    if len(grid) == 0 or len(grid[0]) == 0:
        return 0
    rows, cols = len(grid), len(grid[0])
    q, visit = deque(), set()
    islands = 0

    def dfs(r, c):
        if r not in range(rows) or c not in range(cols) or grid[r][c] == "0" or (r, c) in visit:
            return
        visit.add((r, c))
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, down, up
        for dr, dc in direction:
            dfs(r+dr, c+dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                islands += 1
                dfs(r, c)
    return islands


print(numIslands2([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))

