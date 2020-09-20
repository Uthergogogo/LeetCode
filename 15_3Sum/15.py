def threeSum(nums):
    result = []
    nums.sort()  # Sorting the array takes O(nlog n)
    for i in range(len(nums)-2):
        if nums[i] + nums[i+1] + nums[i+2] > 0:  # 减少不必要的计算 可提速
            break
        if nums[i] + nums[-1] + nums[-2] < 0:
            continue
        if i > 0 and nums[i - 1] == nums[i]:  # 防止重复
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            # 要用temp取代nums[i] + nums[left] + nums[right] 因为如果不用temp则每次都要进行运算 会增加运行时间
            temp = nums[i] + nums[left] + nums[right]
            if temp == 0:
                result.append([nums[i], nums[left], nums[right]])
                # 防止如[-2, 0, 0, 2, 2]等情况会出现两个[-2, 0, 2]的结果
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                left += 1
                # 防止如[-2, 0, 0, 2, 2]等情况会出现两个[-2, 0, 2]的结果
                while right > 0 and nums[right] == nums[right-1]:
                    right -= 1
                right -= 1
            # 双指针正常操作
            elif temp < 0:
                left += 1
            elif temp > 0:
                right -= 1
    return result


print(threeSum([-2,0,1,1,2]))
# print(threeSum([0, 0]))
# print(threeSum([]))
# print(threeSum([0,0,0,0]))
# print(threeSum([-2, 0, 0, 2, 2]))


