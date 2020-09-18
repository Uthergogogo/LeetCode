# 盛最多水的容器  
#### Brute Force
    这就不用多说了8 直接每个都算一遍就完事儿
#### Two Pointer Approach
    这个好牛
    首先left, right存储第一个和最后一个
    每次都对面积进行比较并存储结果
    哪条边长留哪边 另一边就+1或-1
