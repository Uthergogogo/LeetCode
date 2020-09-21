def fourSum(nums, target):
    def kSum(nums, target, k):
        result = []
        # Check if the sum of k smallest values is greater than target, or the sum of k largest values is smaller than target. Since the array is sorted, the smallest value is nums[start], and largest - the last element in nums.
        if len(nums) == 0 or nums[0] * k > target or nums[-1] * k < target:
            return result
        if k == 2:
            return twoSum(nums, target)
        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                for _, set in enumerate(kSum(nums[i+1:], target-nums[i], k-1)):
                    result.append([nums[i]] + set)
        return result

    def twoSum(nums, target):
        result = []
        left, right = 0, len(nums)-1
        while left < right:
            sum = nums[left] + nums[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            else:
                result.append([nums[left], nums[right]])
                left += 1
                right -= 1
        return result

    nums.sort()
    return kSum(nums, target, 4)

print(fourSum([1, 0, -1, 0, -2, 2], 0))