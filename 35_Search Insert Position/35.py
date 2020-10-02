def searchInsert(nums, target):
    if len(nums) == 0:
        return 0
    index = 0
    if target > nums[-1]:
        return len(nums)  # 不能是len(nums)-1 因为是要加到后面 不是取代最后一位
    if target <= nums[0]:
        return 0
    for i in range(len(nums) - 1):
        if target == nums[i + 1]:
            return i + 1
        elif target < nums[i]:
            if i == 0:  # 加速
                return 0
            index = min(index, i)
        elif nums[i] < target < nums[i + 1]:
            return i + 1

    return index