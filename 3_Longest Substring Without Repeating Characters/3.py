# 选用滑动窗口的方法
from collections import defaultdict


def lengthOfLongestSubstring(s):
    # define two pointers
    left, right = 0, 0

    # handle with the situation when there's 0 or 1 element in the string
    if len(s) == 0:
        return 0
    else:
        result = 1

    # create the window and slide it
    window = []
    while right < len(s):
        window.append(s[right])
        result = max(result, len(window))  # can also writen as: result = max(result, right-left+1) because left = 0
        right += 1  # move the window
        while right < len(s) and s[right] in window:
            window.remove(s[left])  # when repeat, remove s[left]
            left += 1  # 缩小window

    return result


def lengthOfLongestSubstring2(s):
    # 更好理解的滑动窗口
    # 且运行效率更高
    """ 运行效率高是 因为在上一个方法中有关于s[right] in window的语句 而python中list in的时间复杂度应该为O(n)
        该方法通过判断出现次数而不是list in提高了运行速度
    """
    left, right = 0, 0
    result = 0
    window = defaultdict(int)

    while right < len(s):
        temp = s[right]
        window[s[right]] += 1  # 该字符每出现一次就记一次数
        right += 1
        while window[temp] > 1:  # 判断是否出现过 不能window[s[right]]是因为right又加了1 此时right可能会outOfRange
            window[s[left]] -= 1
            left += 1  # 移动left缩小窗口
        result = max(result, right-left)
    return result


print(lengthOfLongestSubstring("abcdabcc"))
print(lengthOfLongestSubstring2("abcdabcc"))



