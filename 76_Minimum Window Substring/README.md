# 最小覆盖子串
#### 滑动窗口思想
    首先定义一个窗口 left, right均为0.
    然后开始将这个窗口→, 直至满足条件为止.
    满足条件后开始左移窗口, 每次左移都要对结果进行记录.
    直到再次不满足条件为止则右移窗口. 并重复此过程, 直至right>len(list)为止
###### python的三元运算
    ``` python
       result = a if a<b else b
       # 抽象为 result1 if condition else result2 满足条件则返回第一个 不满足则返回第二个
    ```


