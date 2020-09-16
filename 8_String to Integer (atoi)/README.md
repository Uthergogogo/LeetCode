#字符串转换整数 (atoi)  
    垃圾题目气死我了！！！
    一定要学会用正则！！！
```python
class Solution:
    def myAtoi(self, s: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
```
    ^：匹配字符串开头
    [\+\-]：代表一个+字符或-字符
    ?：前面一个字符可有可无
    \d：一个数字
    +：前面一个字符的一个或多个
    \D：一个非数字字符
    *：前面一个字符的0个或多个
