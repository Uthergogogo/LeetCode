def uniquePathsWithObstacles(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0
    if obstacleGrid[0][0] == 0 and len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
        return 1
    obstacleGrid[0][0] = 1
    for i in range(1, len(obstacleGrid[0])):
        if obstacleGrid[0][i] == 1:
            obstacleGrid[0][i] = 0
            continue
        obstacleGrid[0][i] = obstacleGrid[0][i-1]
    for j in range(1, len(obstacleGrid)):
        if obstacleGrid[j][0] == 1:
            obstacleGrid[j][0] = 0
            continue
        obstacleGrid[j][0] = obstacleGrid[j-1][0]

    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[0])):
            if (i == 0 or j == 0) and i != j:
                continue
            if i > 0 and j > 0 and obstacleGrid[i][j] != 1:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
            else:
                obstacleGrid[i][j] = 0
    return obstacleGrid[len(obstacleGrid)-1][len(obstacleGrid[0])-1]


print(uniquePathsWithObstacles([[0, 0, 1, 0], [1, 0, 1, 0], [1, 0, 0, 0]]))
