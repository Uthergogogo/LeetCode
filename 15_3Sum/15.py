def threeSum(nums):
    result = []
    nums.sort()  # Sorting the array takes O(nlog n)
    for i in range(len(nums)-2):
        if nums[i] + nums[i+1] + nums[i+2] > 0:
            break
        if nums[i] + nums[-1] + nums[-2] < 0:
            continue
        if i > 0 and nums[i - 1] == nums[i]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[i] + nums[left] + nums[right] == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                left += 1
                while right > 0 and nums[right] == nums[right-1]:
                    right -= 1
                right -= 1

            elif nums[i] + nums[left] + nums[right] < 0:
                left += 1
            elif nums[i] + nums[left] + nums[right] > 0:
                right -= 1
    return result


print(threeSum([-2,0,1,1,2]))
# print(threeSum([0, 0]))
# print(threeSum([]))
# print(threeSum([0,0,0,0]))
# print(threeSum([-2, 0, 0, 2, 2]))


