def reverse(x: int) -> int:
    if 0 <= x < pow(2, 31) - 1:
        return int(str(x)[::-1]) if int(str(x)[::-1]) < pow(2, 31) - 1 else 0
    elif 0 > x > -pow(2, 31):
        return -int(str(-x)[::-1]) if -int(str(-x)[::-1]) > -pow(2, 31) else 0
    else:
        return 0

print(reverse(1534236469))