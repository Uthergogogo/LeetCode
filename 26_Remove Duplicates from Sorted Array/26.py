def removeDuplicates(nums):
    # return的是没有重复的元素
    if len(nums) == 0:
        return 0
    else:
        former, res = nums[0], [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == former:
                continue
            else:
                res.append(nums[i])
                former = nums[i]
    return res


def removeDuplicates2(nums):
    # return的是不包含重复的话的长度
    # 按LeetCode的思想 但只是改变了前n位元素的顺序（n为不重复的数量）
    if len(nums) == 0:
        return 0
    else:
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                i += 1
                nums[i] = nums[j]

        return i+1  # 因为i从0开始的


print(removeDuplicates([1,1,1,2, 3, 3, 3, 4]))
print(removeDuplicates2([1,1,1,2, 3, 3, 3, 4]))