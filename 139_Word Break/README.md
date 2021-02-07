#单词拆分
#### 两种Brute Force
    一种是直接的 另一种要缓存 用到了@lru_cache关键字 相当于python自带的缓存机制 不用再创建一个list
#### Dynamic Programming
    if dp[j] and s[j:i] in word_set:
