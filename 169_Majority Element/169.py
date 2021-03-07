from collections import Counter
# count
def majorityElement(nums):
    nums.sort()
    save = dict()
    for i in nums:
        i = str(i)
        if i not in save:
            save[i] = 1
        else:
            save[i] += 1
    max = -float("inf")
    res = 0
    for key, value in save.items():
        if value > max:
            max = value
            res = int(key)
        else:
            continue
    return res

# count by build-in functions
def majorityElement2(nums):
    count = Counter(nums)
    return max(count.keys(), key=count.get)

# sort
def majorityElement3(nums):
    nums.sort()
    needed_length = len(nums)//2
    return nums[needed_length]

# Boyer-Moore Voting Algorithm
def majorityElement4(nums):
    vote, most = 0, nums[0]
    for i in nums:
        if vote == 0:
            most = i
        if i == most:
            vote += 1
        else:
            vote -= 1

    return most


print(majorityElement([3, 2, 3]))
print(majorityElement2([3, 2, 3]))
print(majorityElement3([3, 2, 3]))
print(majorityElement4([3, 2, 3]))