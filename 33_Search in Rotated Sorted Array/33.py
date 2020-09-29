# O(n)
def search(nums, target):
    if target in nums:
        return nums.index(target)
    else:
        return -1


# O(log n)
def search2(nums, target):
    # first need to find where is the rotation by using Binary Search
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] >= nums[left]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(search2([5, 1, 3], 3))
