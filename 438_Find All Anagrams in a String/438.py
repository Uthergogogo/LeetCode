from collections import defaultdict


def findAnagrams(s, p):
    left, right, match, start = 0, 0, 0, []
    window, need = defaultdict(int), defaultdict(int)
    for item in p:
        need[item] += 1
    while right < len(s):
        c1 = s[right]
        if c1 in need.keys():
            window[c1] += 1
            if window[c1] == need[c1]:
                match += 1
        right += 1
        while match == len(need):
            if right - left == len(p):
                start.append(left)
            c2 = s[left]
            if c2 in need.keys():
                window[c2] -= 1
                if window[c2] < need[c2]:
                    match -= 1
            left += 1
    return start


print(findAnagrams("cbaebabacd", "abc"))
