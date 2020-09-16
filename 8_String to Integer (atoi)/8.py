import re

def myAtoi(str):
    return max(min(int(*re.findall('^[\+\-]?\d+', str.lstrip())), 2**31 - 1), -2**31)
