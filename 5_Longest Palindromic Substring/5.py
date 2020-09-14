def longestPalindrome(s):
    if len(s) == 0:
        return ""
    else:
        temp = s[0]
        for i, e in enumerate(s):
            left, right = i, i
            # situation like aba
            while left-1 >= 0 and right+1 < len(s) and s[left-1] == s[right+1]:
                left -= 1
                right += 1
                temp = temp if len(temp) >= len(s[left:right+1]) else s[left:right+1]

            # reset left, right
            left, right = i, i
            # situation like bb, abba, and so on
            while left >= 0 and right+1 < len(s) and s[left] == s[right+1]:
                right += 1
                temp = temp if len(temp) >= len(s[left:right + 1]) else s[left:right + 1]
                left -= 1
        return temp


print(longestPalindrome("babad"))