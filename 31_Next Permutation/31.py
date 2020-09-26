def nextPermutation(nums):
    i, temp,  = len(nums)-1, 0
    while i > 0:
        if nums[i] > nums[i-1]:
            j = len(nums) - 1
            while j >= i:
                if nums[j] > nums[i-1]:
                    temp = nums[j]
                    nums[j] = nums[i - 1]
                    nums[i - 1] = temp
                    nums[i:] = sorted(nums[i:])
                    return 
                j -= 1
        i -= 1
    nums.sort()

print(nextPermutation([1, 8, 9, 7, 6, 5, 4]))
