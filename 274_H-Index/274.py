def hIndex(citations):
    curr = sorted(citations)  # sort the list
    length = len(citations)
    left, right = 0, length - 1
    while left <= right:
        mid = (left + right) // 2
        if curr[mid] == length - mid:
            # when equals, we find the one we need
            return length - mid
        elif curr[mid] < length - mid:
            # when curr[mid]<length - mid, the one we need is at the right of current mid
            left = mid + 1
        else:
            # when curr[mid]>length - mid, the one we need is at the left of current mid
            right = mid - 1

    return length - left


# 也是找到第一个不满足citations[i]>=i+1的i 因为是从0开始 所以要加1
def hIndex2(citations):
    """ another way """
    citations.sort(reverse=True)
    h = 0
    for i in range(len(citations)):
        if citations[i] >= i+1:
            h = i+1
    return h

