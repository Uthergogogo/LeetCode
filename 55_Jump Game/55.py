memo = []

# Dynamic Programming Top-down.


class Solution1:
    def canJump(self, nums):
        for i in range(len(nums)):
            memo.append("UNKNOWN")
        memo[len(nums)-1] = True
        return self.canJumpFromPosition(0, nums)

    def canJumpFromPosition(self, position, nums):
        if memo[position] != "UNKNOWN":
            return memo[position]
        furthestJump = min(position+nums[position], len(nums)-1)
        for i in range(position+1, furthestJump+1):
            if self.canJumpFromPosition(i, nums):
                memo[i] = True
                return True
        memo[position] = False
        return False

# Dynamic Programming Bottom-up


class Solution2:
    memo2 = []

    def canJump(self, nums):
        for i in range(len(nums)):
            self.memo2.append("UNKNOWN")
        self.memo2[len(nums)-1] = True
        for i in range(len(nums)-2, -1, -1):
            furthestJump = min(i+nums[i], len(nums)-1)
            for j in range(i+1, furthestJump+1):
                if self.memo2[j] is True:
                    self.memo2[i] = True
                    break
        return self.memo2[0] is True


# greedy
def canJump(nums):
    lastPos = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= lastPos:
            lastPos = i
    return lastPos == 0

t = Solution1()
tt = Solution2()
print(t.canJump([3, 2, 1, 0, 4]))
print(tt.canJump([3, 2, 1, 0, 4]))
print(canJump([3, 2, 1, 0, 4]))

