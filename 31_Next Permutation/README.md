# 下一个排列
#### one-pass scan
    从最右边开始 直至找到第一个[i-1]>i
    此时j=len(nums) 因为右边永远比左边的小 所以从右开始找到第一个[j]>[i-1]
    将[j]与[i-1]交换位置 并将i往右的sort即可得到结果 nums[i:] = sorted(nums[i:])
###### 注意
    每次用while循环时一定要加上变量的变化 如while i > 0: i -= 1
