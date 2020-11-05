# 不同路径 II  
#### Dynamic Programming
    和62题类似 先进行初始化
    但要考虑更多种情况：
    1. dp[0][0]为1时说明入口就是障碍 此时无法到达目标地点 所以return 0
    2. dp[0][0]为0但长度也为0时 说明入口即为目标地点 所以 return 1
    3. 初始化时第一行标记为1 当遇到障碍（未被标记即为1时）则标记为0 每一个格子的值都=左边的
    4. 初始化时第一列标记为1 当遇到障碍（未被标记即为1时）则标记为0 每一个格子的值都=上边的
    初始化完成后 和62题类似
    dp[i][j] = dp[i-1][j] + dp[i][j-1]
    但是！ 如果遇到某一格子值为1 说明他是墙 那么应该将它标记为0