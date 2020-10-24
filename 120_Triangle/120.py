def minimumTotal(triangle):
    if not triangle or not triangle[0]:
        return 0
    if len(triangle) == 1:
        return triangle[0][0]
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] = triangle[i][j] + min(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]

print(minimumTotal([[-1],[2,3],[1,-1,-3]]))


