# 剑指 Offer 39. 数组中出现次数超过一半的数字
#### 用HashMap遍历并计数
#### built-funtion: Counter
    from collection import Counter
    count = Counter(nums)
    此时count为一个计数完毕的对象
    再通过max(count.keys, key=count.get)来输出value最大的key值
#### sort
    超过一半的数一定在中间
    所以直接把原数组sort 然后return nums[len(nums)//2]即可
#### 摩尔投票法
    初始vote为0
    每当vote为0时则更新众数
    如果当前值==当前众数则vote += 1 否则 -= 1
    可简写为 vote += 1 if i == most else -1
