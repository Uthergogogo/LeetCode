# One-pass Hash Table

def twoSum(numbers, target):
    save = {}
    for index, elem in enumerate(numbers):
        need = target - elem
        if need in save:
            return [save[need], index + 1]
        save[elem] = index + 1

# two pointers

def twoSum2(numbers, target):
    left, right = 0, len(numbers)-1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1

print(twoSum2([1, 3, 4, 5, 6], 11))


