# 合并重叠区间
#### 排序
    首先按照list的第一个元素进行排序
    学一下lambda怎么用！
    intervals.sort(key= lambda x:x[0])意思就是按照第一个元素进行排序
    然后有重叠部分就更新区间
    没有就直接加进去
