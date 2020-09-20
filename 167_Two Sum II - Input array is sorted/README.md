# 两数之和 II - 输入有序数组  
#### one pass Hashtable
    need = target - nums[i]
    if need in save:
        return [save[need], index + 1]
#### 双指针
    一个从0开始 一个从最后一位开始
    如果两数之和小于target left+=1
    大于target right -= 1
