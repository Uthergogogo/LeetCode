def uniquePaths(m, n):
    dp = [[1 for i in range(n)] for j in range(m)]
    dp[0][0] = 0

    for i in range(1, m):
        for j in range(1, n):
            if (m == 0 or n == 0) and m != n:
                continue
            if i > 0 and j > 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp)
    return dp[m-1][n-1]
print(uniquePaths(3, 7))
