def jump(nums):
    n = len(nums)
    if n < 2:
        return 0
    max_pos = nums[0]
    max_step = nums[0]
    jump = 1
    for i in range(1, n):
        if max_step < i:
            jump += 1
            max_step = max_pos
        max_pos = max(max_pos, nums[i]+i)
    return jump