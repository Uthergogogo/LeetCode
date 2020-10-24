# 爬楼梯
#### Dynamic Programming 第一次
    最重要的就是找到转移方程
    对于这道题来说 当前这个台阶可以从前一个或前两个台阶上跳过来
    所以当前的方法 = 前一个的+前两个台阶跳上来的总和
    我们可以知道第一个台阶只有一种跳法 第二个只有两种
    from bottom to top, 那么dp[i] = dp[i-1] + dp[i-2]
    最后返回dp[n]即可
#### 注意
    dp = [0 for i in range(n+1)]
    这里的dp[0]为0 可以忽略
    相当于java的 int[] ll = new int[n+1]
