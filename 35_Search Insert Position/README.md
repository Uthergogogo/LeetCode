#搜索插入位置  
#### one-pass
    有个注意点 target < nums[i]时不能单纯的 index = i 因为可能会比所有的都小
    其次比所有都大时返回的是len(nums)不是len(nums)-1 因为是放到后面不是取代最后一位
