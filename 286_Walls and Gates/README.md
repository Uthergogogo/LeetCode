# 墙与门
#### BFS
    先找到门 并把门加到deque中
    对门进行bfs
    如果找到了在范围内的点且该位置的值是否比上一位置的值+1还要大 如果是的话就更新该位置的值
    并将该位置加入deque中
#### DFS
    也是对门进行dfs 但不用将其加入到deque中了
    如果遇到不满足条件（超出范围/rooms[r][c]<val 说明是墙/已经找到更优解）则return
    否则更新val 并dfs(r+dr, c+dc, val+1)
    但是！为什么r, c = r+dr, c+dc dfs(r, c)不行, dfs(r+dr, c+dc)可以呢？？？
