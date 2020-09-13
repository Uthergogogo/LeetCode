# 找到字符串中所有字母异位词
#### 子串问题优先考虑滑动窗口
    和76题的思路一样 首先双指针left, right
    然后定义窗口和need两个字典（哈希表） 并遍历target将各字符出现次数存储到need里
    开始遍历给定字符串string 如果遇到的字符为target里的字符 则window中该字符出现次数加一
    当该字符出现次数window[s[right]]即s[c1] == need[c1]时match+1 
    不断右移窗口直至所有字符满足条件match == len(need)时
    判断是否满足条件并对结果进行记录 如果s[left]即s[c2] in need.keys() 则 window[s[c2]] -1
    如果window[c2] < need[c2] 则match-1
    左移窗口
    重复右移 判断 左移的操作直至right > len(s)
    
