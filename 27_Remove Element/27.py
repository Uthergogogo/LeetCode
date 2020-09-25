def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1

    return nums[:count]


print(removeElement([1,1,1,2,3,], 1))
