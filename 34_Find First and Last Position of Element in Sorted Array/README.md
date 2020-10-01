# 在排序数组中查找元素的第一个和最后一个位置
#### Binary Search
    看到要求时间复杂度为O(log n)且array是sorted 首选BS
    开始的时候我想着先找到一个 然后往左找直至左边不为target 右边也一样
    但如果0, len(nums)-1也是target的话（worst case） 此时时间复杂度为O(n)
    因此要用两次BS
    left初始化为-1 如果找到的mid为0或nums[mid-1]!=target说明找到了左边界 left=mid
    如果遍历完left还为-1则说明该nums不含有target 返回[-1, -1]
    遍历右边同理 但lo可以从left开始 没必要从0开始了
