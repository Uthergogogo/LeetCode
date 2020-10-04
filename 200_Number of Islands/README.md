# 岛的数量
#### BFS
    这道题是典型的深度/广度优先算法的题。
    广度优先是一直找的符合条件的。
    通过direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]来往四个方位走
    如果遍历到新的符合要求的点就加到visit中记录一下
#### DFS
    和BFS最大的区别是一直找 找到不符合条件的值时return
    然后从上一节点继续找 直到所有的都找完
#### 小tip
    1. for dr, dc in directions:  # direction = [[1, 0], [-1, 0], [0, 1], [0, -1]] 那dr为[][0], dc为[][1]
    2. q = deque() q.append((r, c)) # 如果q里的值是一个元组 row, col = q.popleft()则row为元组第一个值r, col为第二个值c
