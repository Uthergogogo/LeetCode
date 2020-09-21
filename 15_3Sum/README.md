# 三数之和
#### 双指针
    定义一个i 双指针left, right分别等于i+1, len(nums)-1
    要记得用temp取代nums[i]+nums[left]+nums[right]即temp = nums[i]+nums[left]+nums[right]来缩短运行时间
    一定要记得排除重复情况
```python
# [-2, 0, 0, 2, 2]
while left < right and nums[left] == nums[left+1]:
    left += 1  # 当left = 1时 因为nums[left] == nums[left+1] left会变成2
left += 1  # 此时left再加一变为3 所以能避免两个[-2, 0, 2]的情况
while right > 0 and nums[right] == nums[right-1]:
    right -= 1
right -= 1
```
