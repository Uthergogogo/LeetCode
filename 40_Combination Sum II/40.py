# backtracking
def combinationSum2A(candidates, target):
    def backtrack(start, comb, remain):
        if remain == 0:
            res.append(list(comb))
            return
        if remain < 0:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i-1]:
                continue
            elem = candidates[i]
            if elem <= remain:
                comb.append(elem)
                backtrack(i+1, comb, remain-elem)
                comb.pop()
    candidates.sort()
    res = []
    backtrack(0, [], target)
    return res
# DP
def combinationSum2B(candidates, target):
    candidates.sort()
    dp = [set() for _ in range(target + 1)]
    dp[0].add(())
    for num in candidates:
        for tar in range(target, num - 1, -1):
            for item in dp[tar - num]:
                dp[tar].add(item + (num,))
    dp[-1] = [list(i) for i in dp[-1]]
    return [list(i) for i in dp[-1]]
print(combinationSum2B([10,1,2,7,6,1,5], 8))



