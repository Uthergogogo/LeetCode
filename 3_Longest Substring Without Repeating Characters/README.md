# 返回最长不重复子串的长度  
**子串问题优先考虑滑动窗口**  
```python  
# 滑动窗口算法的抽象思想：  

int left = 0, right = 0;

while (right < len(s)):  
    window.add(s[right]);
    right += 1
    
    while (valid) {
        window.remove(s[left]);
        left += 1
    }
}
```

