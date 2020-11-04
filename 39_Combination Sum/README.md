# 组合总和
#### Backtracking
    As a reminder, backtracking is a general algorithm for finding all (or some) solutions to some computational problems. 
    As one can see, the above backtracking algorithm is unfolded as a DFS (Depth-First Search) tree traversal, which is often implemented with recursion.

    Here we define a recursive function of backtrack(remain, comb, start) (in Python), which populates the combinations, starting from the current combination (comb), the remaining sum to fulfill (remain) and the current cursor (start) to the list of candidates. Note that, the signature of the recursive function is slightly different in Java. But the idea remains the same.

    For the first base case of the recursive function, if the remain==0, i.e. we fulfill the desired target sum, therefore we can add the current combination to the final list.

    As another base case, if remain < 0, i.e. we exceed the target value, we will cease the exploration here.

    Other than the above two base cases, we would then continue to explore the sublist of candidates as [start ... n]. For each of the candidate, we invoke the recursive function itself with updated parameters.

    Specifically, we add the current candidate into the combination.

    With the added candidate, we now have less sum to fulfill, i.e. remain - candidate.

    For the next exploration, still we start from the current cursor start.

    At the end of each exploration, we backtrack by popping out the candidate out of the combination.

