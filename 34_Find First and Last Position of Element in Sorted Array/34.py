def searchRange(nums, target):
    # 如果数组为空
    if not nums:
        return [-1, -1]
    # 定义初始边界
    low, high = 0, len(nums) - 1
    left = -1
    right = len(nums) - 1
    # 先找左边
    while low <= high:
        mid = (low + high) >> 1
        # 如果此时的索引对应的值为target，如果是那么有种情况说明这是左边界：1.mid==0时，即数组的最左边。2.当前值左面的值不是目标值
        if nums[mid] == target and (mid == 0 or nums[mid - 1] != target):
            left = mid
            break
        # 正常二分操作
        if nums[mid] < target:
            low = mid + 1
        else:
            # 注意一下这个 else 的操作包括了两种含义：1.nums[mid] > target。2. nums[mid] == target and nums[mid-1] != target 时需要左移
            high = mid - 1
    # 不存在目标值
    if left == -1:
        return [-1, -1]
    # 重新定义区间
    high = len(nums) - 1
    # 此时的左区间就从target的最左区间开始就可以了，没必要从0开始
    low = left
    while low <= high:
        mid = (low + high) >> 1
        # 如果此时的索引对应的值为target，如果是那么有种情况说明这是左边界：1.mid==len(nums)-1时，即数组的最左边。2.当前值左面的值不是目标值
        if nums[mid] == target and (mid == len(nums) - 1 or nums[mid + 1] != target):
            right = mid
            break

        if nums[mid] > target:
            high = mid - 1
        else:
            # 注意一下这个 else 的操作包括了两种含义：1.nums[mid] < target。2. nums[mid] == target and nums[mid+1] != target 时需要右移
            low = mid + 1

    return [left, right]
