# 电话号码的字母组合  
#### 好像叫做backtracking
    主要思路是永远让first和second进行相加
    得出的结果赋值给first 然后让新的first和新second相加直到没有新元素进来
```python
  while pivot < len(digits):
    temp = phone_dict[int(digits[pivot])]
    for item in res:
        for elem in temp:
            curr = item + elem
    nn.append(curr)
    # res = [i + j for i in res for j in temp]
    pivot += 1
    res = nn
    nn = []
```
