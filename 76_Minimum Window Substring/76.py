from collections import defaultdict
import sys


def minWindow(s, t):
    # 先定义好窗口
    left, right, match = 0, 0, 0
    # 因为要输出的是字符串
    start, minLen = 0, sys.maxsize
    # 两个字典用来记录各元素出现次数
    window, need = defaultdict(int), defaultdict(int)
    # 通过该循环记录目标字符串每个字符出现次数
    for i in t:
        need[i] += 1

    while right < len(s):
        c1 = s[right]

        # 如果该字符是所需字符 则给这个字符出现次数+1
        if c1 in need.keys():
            window[c1] += 1
            # 当窗口里该字符的出现次数与所需字符的出现次数刚好相等时 说明这个字符满足条件了
            if window[c1] == need[c1]:
                # match表示的是有几个字符满足了条件
                match += 1
        right += 1
        # 窗口不断右移 直到所有字符满足条件时开始左移窗口 直到不满足条件为止
        while match == len(need):
            if right - left < minLen:
                # start为输出时string的起始位置
                start = left
                # minLen是满足条件最短的子串的长度 不是终止位置！！
                minLen = right - left
            c2 = s[left]
            # 右移时如果即将删掉的是target里的字符 则将窗口中该字符的出现次数-1
            if c2 in need.keys():
                window[c2] -= 1
                # 如果此时该字符不满足条件了 则match-1 此时再次开始右移
                if window[c2] < need[c2]:
                    match -= 1
            left += 1
    # 如果满足条件则输出最小子串 否则输出""
    return "" if minLen == sys.maxsize else s[start: start+minLen]  # 注意 这个是不包括右边界的


