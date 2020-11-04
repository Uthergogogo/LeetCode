def combinationSum(candidates, target):
    res = []

    def backtrack(remain, comb, start):
        if remain == 0:
            res.append(list(comb))
        elif remain < 0:
            return
        for i in range(start, len(candidates)):
            comb.append(candidates[i])
            backtrack(remain - candidates[i], comb, i)
            comb.pop()

    backtrack(target, [], 0)

    return res

print(combinationSum([2, 3, 6, 7], 8))

