def numSquares(n):
    # 动态转移方程为：dp[i] = MIN(dp[i], dp[i - j * j] + 1)，i 表示当前数字，j*j 表示平方数

    if n == 0:
        return 0
    dp = [i for i in range(n+1)]
    dp[0], dp[1] = 0, 1
    for i in range(2, n+1):
        j = 1
        while i - j*j >= 0:
            dp[i] = min(dp[i], dp[i-j*j]+1)
            j += 1
    return dp[-1]


print(numSquares(2))
