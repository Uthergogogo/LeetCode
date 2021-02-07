# Brute Force, O(2^n)
# The naive approach to solve this problem is to use recursion and backtracking. For finding the solution, we check every possible prefix of that string in the dictionary of words, if it is found in the dictionary, then the recursive function is called for the remaining portion of that string. And, if in some function call it is found that the complete string is in dictionary, then it will return true.
from functools import lru_cache


def wordBreak1(s, wordDict):
    def helper(s, word_dict, start):
        if start == len(s):
            return True
        for end in range(start+1, len(s)+1):
            if s[start:end] in word_dict and helper(s, word_dict, end):
                return True
        return False

    return helper(s, set(wordDict), 0)

print(wordBreak1("leetcode", ["leet", "code"]))

# recursion with memorization, O(n^3)
# @lru_cache means an auto cache, no need to create a list and save previous results
def wordBreak2(s, wordDict):
    @lru_cache
    def helper(s, word_dict, start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and helper(s, word_dict, end):
                return True
        return False

    return helper(s, frozenset(wordDict), 0)

print(wordBreak2("leetcode", ["leet", "code"]))

# Dynamic Programming
def wordBreak3(s, wordDict):
    word_set = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[-1]

print(wordBreak3("leetcode", ["leet", "code"]))
