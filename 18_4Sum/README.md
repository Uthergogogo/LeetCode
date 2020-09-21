# 四数之和
#### 双指针
    和二数之和/三数之和类似 都采用双指针的思想
    不过在4Sum中需要进行递归
    直到将kSum递归至two Sum问题后进行运算得出结果。
    如果k = 4, 递归一次之后新target就变成了target - nums[0]
    再递归一次k = 2, 新target= 最初始的target-nums[0]-nums[1]
    需要进行运算的nums变成了nums[2:]
