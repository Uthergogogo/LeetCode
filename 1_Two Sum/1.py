# 双指针
def twoSum(nums, target):
    if len(nums) < 2:
        return -1
    left, right = 0, 1
    while left < len(nums):
        if right >= len(nums):
            left += 1
            right = left + 1
        if nums[left] + nums[right] == target:
            return [left, right]
        right += 1
    return -1

# 确定一个找另一个
def twoSum2(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement not in hash_table:
            hash_table[nums[i]] = i
        else:
            return [hash_table[complement], i]

# 方法三 与二类似. 先把数组每个元素的index和value存到字典里 然后遍历一遍字典找target-nums[i]

print(twoSum2([1, 3, 2, 5, 8], 5))