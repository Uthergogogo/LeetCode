# DP: from bottom to top
def climbStairs(n):
    dp = [0 for i in range(n+1)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# fibonacci
def climbStairs2(n):
    if n <= 1:
        return 1
    if n == 2:
        return 2
    first, second = 1, 2
    res = 0
    while n > 2:
        res = first+second
        first = second
        second = res
        n -= 1
    return res
print(climbStairs2(5))
