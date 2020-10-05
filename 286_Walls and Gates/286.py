from collections import deque

# BFS
# 首先把门的位置都排入 queue 中，然后开始循环，对于门位置的四个相邻点，判断其是否在矩阵范围内，并且位置值是否大于上一位置的值加1，如果满足这些条件，将当前位置赋为上一位置加1，并将次位置排入 queue 中，这样等 queue 中的元素遍历完了，所有位置的值就被正确地更新了
def wallsAndGates(rooms):
    rows, cols = len(rooms), len(rooms[0])

    def bfc(r, c):
        q.append((r, c))
        while q:
            row, col = q.popleft()
            direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in direction:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and rooms[r][c] > rooms[row][col]+1:
                    rooms[r][c] = rooms[row][col] + 1
                    q.append((r, c))
    q = deque()
    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                bfc(r, c)
    return rooms

# DFS
# 搜索0的位置，每找到一个0，以其周围四个相邻点为起点，开始 DFS 遍历，并带入深度值1，如果遇到的值大于当前深度值，将位置值赋为当前深度值，并对当前点的四个相邻点开始DFS遍历，注意此时深度值需要加1，这样遍历完成后，所有的位置就被正确地更新了
def wallsAndGates2(rooms):
    if not rooms:
        return
    rows, cols = len(rooms), len(rooms[0])

    def dfs(r, c, val):
        if r not in range(rows) or c not in range(cols) or rooms[r][c] < val:
            return
        rooms[r][c] = val
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, down, up
        for dr, dc in direction:
            dfs(r+dr, c+dc, val+1)

    for r in range(rows):
        for c in range(cols):
            if rooms[r][c] == 0:
                dfs(r, c, 0)
print(wallsAndGates2([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))
