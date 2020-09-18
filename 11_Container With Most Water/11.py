# Brute Force
def maxArea(height):
    area = 0
    for i in range(len(height)):
        for j in range(1, len(height)):
            area = max(area, (j-i)*min(height[j], height[i]))
    return area


# Two Pointer Approach
def maxArea2(height):
    area, left, right = 0, 0, len(height)-1
    while left < right:
        area = max(area, (right-left)*min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return area

print(maxArea2([1,8,6,2,5,4,8,3,7]))